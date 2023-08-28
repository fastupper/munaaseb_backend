from fastapi import FastAPI
from pydantic import BaseModel
import os
import importlib
import pandas as pd
import json
import numpy as np
import mortgage_formular as mor_formular
import re
import utils


class Mortgage_inputs(BaseModel):
    salary: float
    birthday: str
    sector: str
    supported: bool
    deduction: int
    debtType: str
    debtMonths: int

app = FastAPI()


@app.post("/calculator_mortage/")
async def calc_mortgage(inputs: Mortgage_inputs):
    excel_path = '../client_docs/example_data.xlsx'

    interest_df = pd.read_excel(excel_path,sheet_name='Banks interest')
    print('Number of banks', len(interest_df['Banks Name '].unique()))

    # government_support_df = pd.read_excel(excel_path,sheet_name='Government Support')

    assumption_df = pd.read_excel(excel_path,sheet_name='Assumption', header=None)
    assumption_reader = utils.AssumptionData(assumption_df)
    assumption_reader.get_info()

    applicant_df = pd.read_excel(excel_path,sheet_name='For integration V02')

    headers = applicant_df.iloc[2].values[:341]
    headers = ['' if pd.isna(x) else x for x in headers ] 
    headers = [re.sub(r'[^\w\s]|(?<=\s)_', '', i) for i in headers if type(i)==str]
    match_headers = [i.strip().lower().replace(' ','_') for i in headers if type(i)==str]
    match_headers[match_headers.index('supportednot_supported')] = 'supported_not_supported'
    match_headers[match_headers.index('additional_upfront')] = 'additional_up_front'

    match_headers = [
        col if col != '' else f'col_{i}' 
        for i,col in enumerate(match_headers)
    ]

    print('number of columns:', len(match_headers))

    applicant_df = applicant_df.iloc[3:, :len(match_headers)]
    applicant_df.columns = match_headers # note: col 27 & col 38 both have the same name

    applicant_dicts = applicant_df.to_dict('records')
    print('number of applicants:', len(applicant_dicts))

    applicant_dict = applicant_dicts[0]

    importlib.reload(mor_formular)

    calculator = mor_formular.MortgageCalculator(interest_df)
    
    mortgage_result = calculator.calculate_mortgage(applicant_dict, inputs.model_dump())
    print(mortgage_result)
    # result = calculator.get_mortgage_result()

    # for idx, applicant_dict in enumerate(applicant_dicts):
    #     # calculate
    #     calculator.calculate(applicant_dict)
    #     input_dict = calculator.get_input_dict()
    #     output_flow = calculator.get_output_flow()
    #     pdf_output = calculator.get_pdf_output()
    #     other_dict = calculator.get_other_dict()

    #     # save output
    #     applicant_dir = os.path.join('output', str(idx))
    #     os.makedirs(applicant_dir, exist_ok=True)

    #     with open(os.path.join(applicant_dir, 'input.json'), 'w', encoding='utf-8') as f:
    #         json.dump(input_dict, f, ensure_ascii=False, indent=4)

    #     output_dict = {}
    #     output_dict['input'] = input_dict
    #     output_dict['flow_output'] = output_flow
    #     output_dict['pdf_output'] = pdf_output

    #     with open(os.path.join(applicant_dir, 'output.json'), 'w', encoding='utf-8') as f:
    #         json.dump(output_dict,f, ensure_ascii=False, indent=4)

    return mortgage_result