import streamlit as st
from translate import Translator
import formulas
import openpyxl
import pandas as pd
import numpy as np
import yaml
from tqdm import tqdm
tqdm.pandas()


memory_data = {}
temp_flag = False
verbose = 3 # none, warning, info, debug
input_data = {}

def debug(args):
    if verbose > 2:
        st.text("DEBUG::: " + args)

def info(args):
    if verbose > 0:
        st.text("INFO::: " + args)

def warning(args):
    if verbose > 1:
        st.text("WARNING::: " + args)

def get_cell_info(dataframe, cell_addr):
    '''
    Get cell info from dataframe on the cell address.
    
    return:
        cell_info (dict): the dictionary consist of 
            {sheet, address, value, formula_addr}
        or -1 if not found
    '''

    cell_addr_sheet, cell_addr_id = cell_addr.split('!')
    
    selector = (dataframe['sheet'] == cell_addr_sheet) & (dataframe['address'] == cell_addr_id)
    filtered_df = dataframe.loc[selector]

    if len(filtered_df) > 0:
        cell_info = filtered_df.iloc[0].to_dict()
        return cell_info
    else:
        return -1

def get_cell_value(dataframe, cell_addr):
    '''
    get cell value.

    case ':' in cell_add: array result
    case cell is -1: not found, return -1
    case cell is formular: return formular
    case cell has result value: return result value
    
    '''
    cell_addr_sheet, cell_addr_id = cell_addr.split('!')
    if ':' in cell_addr_id:
        start_cell, end_cell = cell_addr_id.split(':')
        start_col, start_row = openpyxl.utils.cell.coordinate_to_tuple(start_cell)
        end_col, end_row = openpyxl.utils.cell.coordinate_to_tuple(end_cell)

        array_value = []
        for col in range(start_col, end_col + 1 ):
            array_value_col = []
            for row in range(start_row, end_row + 1):
                row_cell_addr = cell_addr_sheet + '!' + openpyxl.utils.cell.get_column_letter(row) + str(col)
                cell_info = get_cell_info(dataframe, row_cell_addr)
                if cell_info == -1:
                    cell_value = -1
                else:
                    cell_value = cell_info['value']

                array_value_col.append(cell_value)
            array_value.append(array_value_col)

        return np.array(array_value)
    else:
        cell_info = get_cell_info(dataframe, cell_addr)
        if cell_info == -1:
            warning(f'get_cell_value: cell_addr: {cell_addr} is not found, return as -1')
            return -1
        elif cell_info['value'].startswith('='):
            return cell_info['formula_addr']
        else:
            return cell_info['value']

def calculate_formula_on_addr(dataframe, cell_addr):
    '''
    Calculate formula through given cell address

    '''

    global memory_data
    global temp_flag



    if cell_addr in memory_data:
        return memory_data[cell_addr]
    else:
        cell_value = get_cell_value(dataframe, cell_addr)
        cell_info = get_cell_info(dataframe, cell_addr)
        
        is_formula = isinstance(cell_value, str) and cell_value.startswith('=')

        if is_formula:
            debug(f"calculate_formula_on_addr: {cell_addr}: {cell_info['value']}")
        else:
            debug(f"calculate_formula_on_addr: {cell_addr}: {cell_value}")
        
        if is_formula:
            try:
                func = formulas.Parser().ast(cell_value)[1].compile()
            except Exception as e:
                st.error(f'The formular is not passable: {cell_value}')
                raise e

            func_input_addrs = list(func.inputs)
            
            func_inputs = []
            temp_input = {}
            for func_input_addr in func_input_addrs:
                func_input_addr = func_input_addr.replace('ASSUMPTION', 'Assumption').replace('For_integration_V02'.upper(), 'For_integration_V02')
                func_input_calc_value = calculate_formula_on_addr(dataframe, func_input_addr)
                
                memory_data[func_input_addr] = func_input_calc_value
                func_inputs.append(func_input_calc_value)
                temp_input[func_input_addr.upper()] = func_input_calc_value
            
            calc_value = func(*func_inputs)
            if isinstance(calc_value, formulas.functions.Array):
                calc_value = calc_value.tolist()
            if isinstance(calc_value, float) and calc_value.is_integer():
                calc_value = str(int(calc_value))

            calc_info = f"calculate_formula_on_addr: calc_result: "
            calc_info += f'\n\tcell_addr: {cell_addr}'
            calc_info += f'\n\tcell_value: {cell_value}'
            calc_info += f'\n\tfunc_input: '
            for tfunc_input_addr, func_input in zip(func_input_addrs, func_inputs):
                func_input_ = str(func_input).replace("\n", "")
                calc_info += f'\n\t\t{tfunc_input_addr}: {str(type(func_input))}: {func_input_}'
            calc_info += f'\n\tcalc_value: {calc_value}'
            debug(calc_info)
            
            if cell_addr == 'For_integration_V02!BH5':
                if len(calc_value) == 1:
                    calc_value = calc_value[0]
                if len(calc_value) == 1:
                    calc_value = calc_value[0]
                st.write(calc_value)

            calculation_error = False
            if isinstance(calc_value, list):
                if len(calc_value) > 0:
                    if len(calc_value[0]) > 0:
                        if isinstance(calc_value[0][0], formulas.tokens.operand.XlError):
                            calculation_error = True

            if not calculation_error:
                return calc_value
            else:
                return -1
        else:
            memory_data[cell_addr] = cell_value
            return cell_value


# init
st.header('Calculator')
translator_zh = Translator(to_lang="zh", from_lang='ar')
formula_csv_path = '../output/formula.csv'
config_path = 'main.yml'

with open(config_path, 'r') as fid:
    calc_config = yaml.safe_load(fid.read())

# read formula csv
formula_df = pd.read_csv(formula_csv_path)
calc_config_input_keys = [k for k in list(calc_config['input'].keys())]

# get default values
recorded_dict = {}
for input_key_addr in calc_config_input_keys:
    input_key_value_addr = input_key_addr.replace('4', '5')

    cell_value = get_cell_value(formula_df, input_key_value_addr)
    if cell_value != -1:
        recorded_dict[input_key_addr] = cell_value

# st.write(f"------------------> {recorded_dict}")

# display input data
for input_title_addr, input_type in calc_config['input'].items():
    if input_title_addr != '':
        title_cell = get_cell_value(formula_df, input_title_addr)
        if title_cell == -1: continue

    default_value = recorded_dict.get(input_title_addr, '')
    if input_type == 'str':
        memory_data[input_title_addr.replace('4', '5')] = st.text_input(title_cell, value=default_value)
    input_data[input_title_addr.replace('4', '5')] = title_cell

if verbose > 2:
    st.write(memory_data)
    st.write(", ".join(list(input_data.values())))
st.write('---')

# display calculated output data
for output_title_addr, output_formula_addr in calc_config['output'].items():
    if output_title_addr != '':  
        title_cell = get_cell_value(formula_df, output_title_addr)

    if verbose > 2:
        with st.expander('info'):

            calc_value = calculate_formula_on_addr(formula_df, output_formula_addr)
            if calc_value != -1:
                memory_data[output_formula_addr] = calc_value

            info(f'{output_title_addr}: {title_cell}')

            cell_value = get_cell_value(formula_df, output_formula_addr)
            info(f"{output_formula_addr}: {cell_value}")
            info(f"result: {calc_value}")

    st.text(f'{title_cell} ({output_formula_addr})')
    st.code(calc_value)