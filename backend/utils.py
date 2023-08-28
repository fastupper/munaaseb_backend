import pandas as pd


class ExcelReader:
    def __init__(self, dataframe: pd.DataFrame):
        self.data = dataframe
    
    def separate_cell_id(self, cell_id: str):
        col_str, row_str = '', ''
        for char in cell_id:
            if char.isalpha():
                col_str += char
            elif char.isdigit():
                row_str += char
        return col_str, row_str
    
    def convert_alphabet_to_number(self, alphabet: str) -> int:
        alphabet = alphabet.upper()
        col_num = 0
        for i, char in enumerate(alphabet[::-1]):
            col_num += (ord(char) - ord('A') + 1) * (26 ** i)
        return col_num

    def get_cell_item(self, cell_id: str) -> object:
        col_str, row_str = self.separate_cell_id(cell_id)
        col = self.convert_alphabet_to_number(col_str) - 1
        row = int(row_str) - 1 

        data = self.data.iloc[col, row]
        if pd.isna(data):
            return None
        
        return data


class AssumptionData:
    def __init__(self, dataframe: pd.DataFrame):
        self.reader = ExcelReader(dataframe)

        self.info_cell = {
            "Max Acceptable age": 'C2',
            "النسبة للمجموعة الأولى من الأفراد": 'C3',
            "Min Down PMT": 'C4',
            "Increase in support % for a unit increased": 'C5',
            "Max No. of years": 'C6',
            "Personal Loan Interest": 'C7',
        }

    def get_info(self) -> dict:
        return {
            k:self.reader.get_cell_item(v) 
            for k,v in self.info_cell.items()
        }
