from fastapi import FastAPI, Query, Path
from pydantic import BaseModel
import os
import importlib
import pandas as pd
import json
import numpy as np
import mortgage_formular as mor_formular
import re
import utils
from typing import Annotated
from fastapi.middleware.cors import CORSMiddleware
from hijri_converter import Hijri
import datetime


class Mortgage_inputs(BaseModel):
    salary: Annotated[float, Query(gt=0)]
    birthday: str
    sector: str
    militaryType: Annotated[str | None, Query(default=None)]
    supported: bool
    deduction: Annotated[int, Query(gt=0, le=65)]
    debtType: str
    debtMonths: Annotated[int, Query(ge=7)]

app = FastAPI()

origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/calculator_mortgage/")
async def calc_mortgage(inputs: Mortgage_inputs):
    inputs = inputs.model_dump()
    hijri_date = inputs['birthday']
    print('==>', inputs)
    if inputs['sector'] == 'military':
        military_type = inputs['militaryType']

    # militaryCap = {
    #     "جندي": 44,
    #     "جندي اول": 44,
    #     "عريف": 46,
    #     "وكيل رقيب": 48,
    #     "رقيب": 50,
    #     "رقيب اول": 50,
    #     "رئيس رقباء": 52,
    #     "ملزم": 44,
    #     "ملزم اول": 44,
    #     "نقيب": 48,
    #     "رائد": 50,
    #     "مقدم": 52,
    #     "عقيد": 54,
    #     "عميد": 56,
    #     "لواء": 58
    # }

    militaryCap = {
        "soldier": 44,
        "first_soldier": 44,
        "corporal": 46,
        "sergeant_agent": 48,
        "Sergeant": 50,
        "staff_sergeant": 50,
        "chief_sergeants": 52,
        "staff": 44,
        "obliged_first": 44,
        "captain": 48,
        "pioneer": 50,
        "forerunner": 52,
        "colonel": 54,
        "dean": 56,
        "major_general": 58
    }


    print('-------->', militaryCap[military_type])

    hijri_birth_year = hijri_date.split('/')[0]
    hijri_birth_month = hijri_date.split('/')[1]
    hijri_birth_day = hijri_date.split('/')[2]
    gregorian_birth = Hijri(int(hijri_birth_year), int(hijri_birth_month), int(hijri_birth_day)).to_gregorian()
    today = datetime.date.today()
    age = today.year - gregorian_birth.year - ((today.month, today.day) < (gregorian_birth.month, gregorian_birth.day))
    if inputs['sector'] == 'civilian' and age > 60:
        return {'error': 'Can not provide mortgage for a person over 60 years old'}
    
    if inputs['sector'] == 'military' and age > militaryCap[military_type]:
        return {'error': 'Can not provide mortgage because of the age'}
    

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
    
    mortgage_result = calculator.calculate_mortgage(applicant_dict, inputs)
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