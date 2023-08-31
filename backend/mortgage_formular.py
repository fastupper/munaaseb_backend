"""
O5 = Home_price
BD5 = Debt Qualified
BX5 = Aff_Max_DP Max Mortgage loan AMT
Assumption G3 = 800000
Assumption G4 = 0.05
Assumption C2 = 70
Assumption C4 = 0.1
Assumption C6 = 30

M5 = Age
BU5 = Aff_Max_DP Interest
BT5 = Aff_Max_DP No. of available years
BW5 = Aff_Max_DP PMT Calc
CD5 = Aff_Max_DP Down PMT
BR5 = Available Salary
BV5 = Aff_Max_DP Total Paid AMT

### Flow output
additional_up_front = IF(O5>BX5,IF(O5-BX5>BD5,O5-BX5,O5-BX5+BD5),0)
debt qualified = IF($O5<=Assumption!$G$3,$O5*Assumption!$G$4,$O5*Assumption!$C$4)
Aff_Max_DP No. of available years = IF((Assumption!$C$2-M5)>Assumption!$C$6,Assumption!$C$6,Assumption!$C$2-M5)
aff_max_dp_max_mortgage_loan_amt = PV(BU5/12,BT5*12,-BW5)
Aff_Max_DP Max Debt AMT = BX5+CD5
Aff_Max_DP Monthly PMT = BR5
Aff_Max_DP Total Interest = BV5-BX5
Aff_Max_DP Down PMT = IF($O5<=Assumption!$G$3,(BX5/(1-Assumption!$G$4))-BX5,(BX5/(1-Assumption!$C$4))-BX5)
"""

"""
Calculates the present value of an investment based on the specified arguments.

Arguments:
    rate -- interest rate per period
    nper -- total number of payment periods in an investment
    pmt -- payment made each period
    fv (optional) -- future value or cash balance after the last payment is made (default is 0)
    type (optional) -- specifies when payments are due (0 for end of period, 1 for beginning of period; default is 0)
        P: Payment made each period
        r: Interest rate per period (usually expressed as a percentage, but entered as a decimal value in the formula)
        n: Total number of payment periods
Returns:
    present value of the investment
"""

"""
PDF output
Supporting Merit % = IF($Q5=Assumption!$F$10,BN5,0)

mor_10_ndp_no_of_available_years = self.years
mor_10_ndp_interest = 
ARRAY_CONSTRAIN(ARRAYFORMULA(INDEX(Assumption!$C$11:$I$36,MATCH(IM5,Assumption!$B$11:$B$36,0),MATCH($Q5,Assumption!$C$10:$I$10,0))), 1, 1)
mor_10_ndp_principle_amt = 
mor_10_ndp_debt_amt = 
mor_10_ndp_monthly_pmt = 
mor_10_ndp_total_paid_amt = 
mor_10_ndp_total_interest = 
mor_10_ndp_down_pmt = 
mor_10_ndp_personal_loan_interest = 
mor_10_ndp_no_of_years = 
mor_10_ndp_monthly_pl_pmt = 
mor_10_ndp_total_pl_paid_amt = 
mor_10_ndp_total_pl_interest = 
mor_10_ndp_total_monthly_pmt = 
mor_10_ndp_age_qualification = 
mor_10_ndp_pmt_qualification = 
mor_10_ndp_pmt = 
mor_10_ndp__of_supported_years = 
mor_10_ndp_monthly_support_and_principle = 
mor_10_ndp_support_and_interest = 
mor_10_ndp_full_interest_to_cover = 
mor_10_ndp_covered_interest = 
mor_10_ndp_monthly_support = 
mor_10_ndp_monthly_pmt_after_support = 
mor_10_ndp_total_paid_amt_after_support = 

Aff_Max_DP No. of available years = ARRAY_CONSTRAIN(ARRAYFORMULA(INDEX(Assumption!$C$11:$I$36,MATCH($BT5,Assumption!$B$11:$B$36,0),MATCH($Q5,Assumption!$C$10:$I$10,0))), 1, 1)
Aff_Max_DP Total Paid AMT = (BR5*12*BS5)+((BT5-BS5)*J5*BQ5*12)
mor_10_dp_no_of_available_years = 10
Mor_10_DP Interest = ARRAY_CONSTRAIN(ARRAYFORMULA(INDEX(Assumption!$C$11:$I$36,MATCH($BT5,Assumption!$B$11:$B$36,0),MATCH($Q5,Assumption!$C$10:$I$10,0))), 1, 1)
Mor_10_DP Principle AMT =$O5-$BC5
Mor_10_DP debt AMT =PV(DX5/12,DW5*12,(-EA5))
Mor_10_DP Monthly PMT = MIN(EB5,$BR5)
Mor_10_DP Total Paid AMT = IF(ED5="Scenario",FV(0,DW5*12,-EB5),FV(0,DW5*12,-EA5))
Mor_10_DP Total Interest = EE5-DZ5
Mor_10_DP Down PMT = EH5+EI5
Mor_10_DP Age Qualification  = IF(DW5>$BT5,"غير مؤهل","مؤهل")
Mor_10_DP PMT Qualification  = IF((EA5+$K5)/$J5<=$BQ5,"مؤهل","غير مؤهل")
Mor_10_DP PMT % = (EA5+$K5)/$J5
Mor_10_DP # of supported years = IF(DW5<Assumption!$J$7,DW5,Assumption!$J$7)
Mor_10_DP Monthly support and Principle = PMT(DX5/12,DW5*12,-$BI5)
Mor_10_DP Support and interest = FV(0,EM5*12,-EN5)
Mor_10_DP full interest to cover = EO5-$BI5
Mor_10_DP Covered interest = EP5*$BO5
Mor_10_DP Monthly support = EQ5/(EM5*12)
Mor_10_DP Monthly PMT after support = EA5-ER5
Mor_10_DP Total Paid AMT after support = EE5-EQ5

mor_15_dp_no_of_available_years = 15
Mor_15_DP Interest = ARRAY_CONSTRAIN(ARRAYFORMULA(INDEX(Assumption!$C$11:$I$36,MATCH($BT5,Assumption!$B$11:$B$36,0),MATCH($Q5,Assumption!$C$10:$I$10,0))), 1, 1)
Mor_15_DP Principle AMT =$O5-$BC5
Mor_15_DP debt AMT =PV(EV5/12,EU5*12,(-EY5))
Mor_15_DP Monthly PMT =MIN(EZ5,$BR5)
Mor_15_DP Total Paid AMT = IF(FB5="Scenario",FV(0,EU5*12,-EZ5),FV(0,EU5*12,-EY5))
Mor_15_DP Total Interest = FC5-EX5
Mor_15_DP Down PMT = FF5+FG5
Mor_15_DP Age Qualification  = IF(EU5>$BT5,"غير مؤهل","مؤهل")
Mor_15_DP PMT Qualification  = IF((EY5+$K5)/$J5<=$BQ5,"مؤهل","غير مؤهل")
Mor_15_DP PMT % = (EY5+$K5)/$J5
Mor_15_DP # of supported years = IF(EU5<Assumption!$J$7,EU5,Assumption!$J$7)
Mor_15_DP Monthly support and Principle = PMT(EV5/12,EU5*12,-$BI5)
Mor_15_DP Support and interest = FV(0,FK5*12,-FL5)
Mor_15_DP full interest to cover = FM5-$BI5
Mor_15_DP Covered interest = FN5*$BO5
Mor_15_DP Monthly support = FO5/(FK5*12)
Mor_15_DP Monthly PMT after support = EY5-FP5 (EA5-ER5)
Mor_15_DP Total Paid AMT after support = FC5-FO5 (EE5-EQ5)
"""

import numpy as np
import numpy_financial as npf
import pandas as pd
from hijri_converter import Hijri
import datetime


class MortgageCalculator:
    
    def __init__(self, interest_df):
        self.aspt_g3 : int = 800000
        self.aspt_g4 : float = 0.05
        self.aspt_c2 : int = 70
        self.aspt_c4 : float = 0.1
        self.aspt_c6 : int = 30
        
        self.aspt_f10 = 'مستحق للدعم'
        self.aspt_j7 = 20
        self.interest_df = interest_df


    def __interest_rate(self, year, bank_name, supported_not_supported):
        if supported_not_supported:
            isSupported = 'مستحق للدعم'
        else:
            isSupported = 'غير مستحق للدعم'
        selector = self.interest_df['Banks Name '] == bank_name
        # if year == 'max':
        #     selector &= self.interest_df['Num of year '] == self.interest_df['Num of year '].max()
        # else:
        #     selector &= self.interest_df['Num of year '] == year
        interest_rates = self.interest_df.loc[selector, isSupported].values

        if len(interest_rates) <= 0:
            error_msg = f'Interest rate not found: {bank_name}, {year}, {supported_not_supported}'
            raise ValueError(error_msg)

        return interest_rates[0]


    def __dict_to_report(self, data: dict) -> dict:
        for i in data.keys():
            if pd.isnull(data[i]):
                data[i] = "0"
            else:
                try:
                    value = float(data[i])
                    if value < 1 and value > 0:
                        data[i] = '{:.02f}%'.format(value*100)
                    else:
                        data[i] = '{:,.02f}'.format(value)
                except ValueError:
                    pass
        return data


    def calculate(self, applicant_dict):
        report_data = {}

        # input data
        report_data['mobile_number'] = applicant_dict['mobile_number']
        report_data['first_name'] = applicant_dict['first_name']
        report_data['last_name'] = applicant_dict['last_name']
        report_data['nationality'] = applicant_dict['nationality']
        report_data['national_id'] = applicant_dict['national_id']
        report_data['employer'] = applicant_dict['employer']
        report_data['desirable_city'] = applicant_dict['desirable_city']
        report_data['customer_bank_name'] = applicant_dict['customer_bank_name']
        report_data['customer_partner_bank_name'] = applicant_dict['customer_partner_bank_name']
        report_data['salary'] = applicant_dict['salary']
        report_data['other_debt'] = applicant_dict['other_debt']
        report_data['age'] = applicant_dict['age']
        report_data['years_to_borrow_over'] = applicant_dict['years_to_borrow_over']
        report_data['home_price'] = applicant_dict['home_price']
        report_data['home_searching_status'] = applicant_dict['home_searching_status']
        report_data['supported_not_supported'] = applicant_dict['supported_not_supported']
        report_data['working_sector'] = applicant_dict['working_sector']
        report_data['is_this_your_first_time_purchasing_home'] = applicant_dict['is_this_your_first_time_purchasing_home']
        report_data['no_of_people_applying_for_this_mportgage'] = applicant_dict['no_of_people_applying_for_this_mportgage']
        report_data['do_you_have_down_payment'] = applicant_dict['do_you_have_down_payment']
        report_data['interested_area_of_the_city'] = applicant_dict['interested_area_of_the_city']
        report_data['family_members'] = applicant_dict['family_members']
        report_data['whatsapp_name'] = applicant_dict['whatsapp_name']
        report_data['advert_filter'] = applicant_dict['advert_filter']
        report_data['action_feedback'] = applicant_dict['action_feedback']
        report_data['action_reasoning'] = applicant_dict['action_reasoning']
        report_data['subscription_status'] = applicant_dict['subscription_status']
        report_data['advertiser_name'] = applicant_dict['advertiser_name']
        report_data['advertiser_city'] = applicant_dict['advertiser_city']
        report_data['advertiser_number'] = applicant_dict['advertiser_number']
        report_data['user_consent'] = applicant_dict['user_consent']

        # other dict
        columns = ['aff_max_dp_max_mortgage_loan_amt',
                   'aff_max_dp_interest',
                   'aff_max_dp_pmt_calc',
                   'aff_max_dp_down_pmt',
                   'aff_max_dp_monthly_pmt',
                   'available_salary',
                   'aff_max_dp_total_paid_amt',
                   'max_debt',
                   'debt_years_conf',
                   'مبلغ_الدعم',
                   'تاكيد_الحسبة',
                   ]
        
        columns_prefix = ['debt_assumption',
                          'pv_debt',
                          'full_interest_to_cover',
                          'covered_interest',
                          '_of_supported_years',
                          'old_dp',
                          'scenario_dp',
                          ]

        for year in [10,15,20,25,'max']:
            prefix = f'mor_{year}_dp_'
            for col in columns_prefix:
                columns.append(prefix + col)

        for col in columns:
            report_data[col] = applicant_dict.get(col)

        # outputflow
        if report_data.get('home_price') > report_data.get('aff_max_dp_max_mortgage_loan_amt'):
            if report_data.get('home_price')-report_data.get('aff_max_dp_max_mortgage_loan_amt') > report_data.get('debt_qualified'):
                additional_up_front = report_data.get('home_price')-report_data.get('aff_max_dp_max_mortgage_loan_amt')
            else:
                additional_up_front = report_data.get('home_price')-report_data.get('aff_max_dp_max_mortgage_loan_amt')+report_data.get('debt_qualified')
        else:
            additional_up_front = 0
        report_data['additional_up_front'] = additional_up_front

        if report_data.get('home_price') <= self.aspt_g3:
            report_data['debt_qualified'] = report_data.get('home_price')*self.aspt_g4
        else:
            report_data['debt_qualified'] = report_data.get('home_price')*self.aspt_c4

        if (self.aspt_c2-report_data.get('age')) > self.aspt_c6:
            report_data['aff_max_dp_no_of_available_years'] = self.aspt_c6
        else:
            report_data['aff_max_dp_no_of_available_years'] = self.aspt_c2-report_data.get('age')

        rate = report_data.get('aff_max_dp_interest')/12
        pmt = -report_data.get('aff_max_dp_pmt_calc')
        nper = report_data.get('aff_max_dp_no_of_available_years')*12
        report_data['aff_max_dp_max_mortgage_loan_amt'] = npf.pv(rate, nper, pmt)
    
        report_data['aff_max_dp_max_debt_amt'] = report_data.get('aff_max_dp_max_mortgage_loan_amt') + report_data.get('aff_max_dp_down_pmt')
        report_data['aff_max_dp_monthly_pmt'] = report_data.get('available_salary')
        report_data['aff_max_dp_total_interest'] = report_data.get('aff_max_dp_total_paid_amt') - report_data.get('aff_max_dp_max_mortgage_loan_amt')
    
        if (report_data.get('home_price') <= self.aspt_g3):
            denom = 1-self.aspt_g4
        else:
            denom = 1-self.aspt_c4                                
        report_data['aff_max_dp_down_pmt'] = (report_data.get('aff_max_dp_max_mortgage_loan_amt')/denom)-report_data.get('aff_max_dp_max_mortgage_loan_amt')

        # pdfoutput        
        supported_not_supported = report_data.get('supported_not_supported')
        تاكيد_الحسبة = report_data.get('تاكيد_الحسبة')
        if supported_not_supported == self.aspt_f10:
            supporting_merit = تاكيد_الحسبة
        else:
            supporting_merit = 0
        report_data['supporting_merit'] = supporting_merit
        
        report_data['aff_max_dp_interest'] = 0.0394
        
        available_salary = report_data.get('available_salary')
        debt_years_conf = report_data.get('debt_years_conf')
        aff_max_dp_no_of_available_years = report_data.get('aff_max_dp_no_of_available_years')
        max_debt = report_data.get('max_debt')
        report_data['aff_max_dp_total_paid_amt'] = (available_salary * 12 * debt_years_conf) + ((aff_max_dp_no_of_available_years - debt_years_conf) * available_salary * max_debt * 12)
        
        for year in [10,15,20,25,'max']:
            prefix = f'mor_{year}_dp_'

            if year == 'max':
                year = report_data.get('aff_max_dp_no_of_available_years')
            report_data[prefix + 'no_of_available_years'] = year

            interest_rate = self.__interest_rate(year, report_data.get('customer_bank_name'), supported_not_supported)
            report_data[prefix + 'interest'] = interest_rate
        
            home_price = report_data.get('home_price')
            addition_up_front = report_data.get('additional_up_front')
            report_data[prefix + 'principle_amt'] = home_price-addition_up_front
        
            if year == 10:
                pv_debt = report_data.get(prefix + 'debt_assumption')
            else:
                pv_debt = report_data.get(prefix + 'pv_debt')

            rate = interest_rate / 12
            num_periods = year * 12
            present_value = pv_debt
            dp_pv_pmt = npf.pmt(rate, num_periods, -present_value)
            report_data[prefix + 'monthly_pmt'] = np.min([dp_pv_pmt, available_salary])
        
            nper = year * 12
            pmt = -report_data[prefix + 'monthly_pmt']
            report_data[prefix + 'debt_amt'] = npf.pv(interest_rate / 12, nper, pmt)
        
            interest_rate_ = 0.12
            if report_data.get(prefix + 'scenario_or_aff') == "Scenario":
                pmt = -dp_pv_pmt
            else:
                pmt = -report_data[prefix + 'monthly_pmt']
            report_data[prefix + 'total_paid_amt'] = npf.fv(interest_rate_, nper, pmt, 0)
    
            report_data[prefix + 'total_interest'] = report_data.get(prefix + 'total_paid_amt') - report_data.get(prefix + 'debt_amt')
            
            old_dp = report_data.get(prefix + 'old_dp')
            scenario_dp = report_data.get(prefix + 'scenario_dp')
            report_data[prefix + 'down_pmt'] = old_dp + scenario_dp
        
            if year > aff_max_dp_no_of_available_years:
                report_data[prefix + 'age_qualification'] = "غير مؤهل"
            else:   
                report_data[prefix + 'age_qualification'] = "مؤهل"

            other_debt = report_data.get('other_debt')
            salary = report_data.get('salary')
            if ((report_data[prefix + 'monthly_pmt'] + other_debt) / salary) <= max_debt:
                report_data[prefix + 'pmt_qualification'] = "مؤهل"
            else:
                report_data[prefix + 'pmt_qualification'] = "غير مؤهل"
        
            pmt = (report_data[prefix + 'monthly_pmt'] + other_debt) / salary
            report_data[prefix + 'pmt'] = pmt
        
            if year < self.aspt_j7:
                report_data[prefix + '_of_supported_years'] = year
            else:
                report_data[prefix + '_of_supported_years'] = self.aspt_j7
        
            pv = -report_data.get('مبلغ_الدعم')
            report_data[prefix + 'monthly_support_and_principle'] = npf.pmt(interest_rate/12, nper, pv)
        
            interest_rate_ = 0.12
            nper = report_data[prefix + '_of_supported_years'] * 12
            pmt = -report_data[prefix + 'monthly_support_and_principle']
            pv = 0
            report_data[prefix + 'support_and_interest'] = npf.fv(interest_rate_, nper, pmt, pv)
            report_data[prefix + 'full_interest_to_cover'] = report_data.get(prefix + 'support_and_interest') - report_data.get('مبلغ_الدعم')
            report_data[prefix + 'covered_interest'] = report_data.get(prefix + 'full_interest_to_cover') * supporting_merit
            report_data[prefix + 'monthly_support'] = report_data.get(prefix + 'covered_interest')/ (report_data.get(prefix + '_of_supported_years') * 12)
            report_data[prefix + 'monthly_pmt_after_support'] = report_data.get(prefix + 'monthly_pmt') - report_data.get(prefix + 'monthly_support')
            report_data[prefix + 'total_paid_amt_after_support'] = report_data.get(prefix + 'total_paid_amt') - report_data.get(prefix + 'covered_interest')
        
            # other calculation
            # home searching status
            home_searching_status = report_data.get('home_searching_status')
            if home_searching_status == 'found': 
                if report_data.get('debt_classification') == 'not eligible':
                    home_searching_status = 'searching'
            report_data[prefix + 'home_searching_status'] = home_searching_status

            # should have male >= 60 & female >= 55
            is_pensioner = report_data.get('age') >= 60
            house_debt_rate = report_data.get(prefix + 'monthly_pmt') / report_data.get('salary')
            full_debt_rate = (report_data.get(prefix + 'monthly_pmt') + report_data.get('other_debt')) / report_data.get('salary')

            cat1_full_debt_rate = 0.55
            cat2_full_debt_rate = 0.65

            debt_classification = [
                report_data[prefix + 'home_searching_status'],
                report_data['do_you_have_down_payment'],
                report_data['other_debt'],
                '>2000' if report_data['available_salary'] > 2000 else '<=2000',
            ]
            report_data[prefix + 'debt_classification'] = '{} {} {} {}'.format(*debt_classification)
        
        self.report_data = report_data



    def calculate_mortgage(self, applicant_dict, inputs):
        hijri_birth_year = inputs['birthday'].split('/')[0]
        hijri_birth_month = inputs['birthday'].split('/')[1]
        hijri_birth_day = inputs['birthday'].split('/')[2]
        gregorian_birth = Hijri(int(hijri_birth_year), int(hijri_birth_month), int(hijri_birth_day)).to_gregorian()
        today = datetime.date.today()
        age = today.year - gregorian_birth.year - ((today.month, today.day) < (gregorian_birth.month, gregorian_birth.day))
        report_data = {}

        # input data

        report_data['salary'] = inputs['salary']
        report_data['debt_years'] = inputs['debtMonths'] / 12
        report_data['age'] = age
        report_data['debt_type'] = inputs['debtType']
        report_data['supported_not_supported'] = inputs['supported']
        report_data['working_sector'] = inputs['sector']
        report_data['deduction_percentage'] = inputs['deduction']
        report_data['customer_bank_name'] = 'البلاد'

        # The principal amount of the loan

        interest_rate = self.__interest_rate(report_data['debt_years'], report_data['customer_bank_name'], report_data['supported_not_supported'])
        monthly_payment = report_data['salary'] * (report_data['deduction_percentage'] / 100)
        principal_amount = -npf.pv(interest_rate / 12, report_data['debt_years'] * 12, monthly_payment)
        total_payment = monthly_payment * report_data['debt_years'] * 12
        profit = total_payment - principal_amount
        # print('interest_rate', interest_rate)
        # print('monthly_payment', monthly_payment)
        # print('principal_amount', principal_amount)
        # print('total_payment', total_payment)
        # print('profit', profit)
        result_mortgage = {
            "installment": monthly_payment,
            "total_loan_amount": principal_amount,
            "period": inputs['debtMonths'],
            "total_profit": profit,
            "interest_rate": interest_rate
        }
        return result_mortgage


    def get_input_dict(self):
        input_dict_columns = [
            'mobile_number',
            'first_name',
            'last_name',
            'nationality',
            'national_id',
            'employer',
            'desirable_city',
            'customer_bank_name',
            'customer_partner_bank_name',
            'salary',
            'other_debt',
            'age',
            'years_to_borrow_over',
            'home_price',
            'home_searching_status',
            'supported_not_supported',
            'working_sector',
            'is_this_your_first_time_purchasing_home',
            'no_of_people_applying_for_this_mportgage',
            'do_you_have_down_payment',
            'interested_area_of_the_city',
            'family_members',
            'whatsapp_name',
            'advert_filter',
            'action_feedback',
            'action_reasoning',
            'subscription_status',
            'advertiser_name',
            'advertiser_city',
            'advertiser_number',
            'user_consent',
        ]

        return self.__dict_to_report({
            k : v
            for k,v in self.report_data.items()
            if k in input_dict_columns
        })


    def get_output_flow(self):
        output_flow_columns = [
            'additional_up_front',
            'debt_qualified',
            'aff_max_dp_no_of_available_years',
            'aff_max_dp_max_mortgage_loan_amt',
            'aff_max_dp_max_debt_amt',
            'aff_max_dp_monthly_pmt',
            'aff_max_dp_total_interest',
            'aff_max_dp_down_pmt',
        ]

        return self.__dict_to_report({
            k : v
            for k,v in self.report_data.items()
            if k in output_flow_columns
        })
    
    def get_mortgage_result(self):
        mortgage_result_colums = [
            'loan_amount',
            'profit',
            'debt_years',
            'installment'
        ]

        return self.__dict_to_report({
            k : v
            for k,v in self.report_data.items()
            if k in mortgage_result_colums
        })

    def get_pdf_output(self):
        pdf_output_columns = [
            'supporting_merit',
            'aff_max_dp_interest',
            'aff_max_dp_total_paid_amt',
            'mor_10_dp_no_of_available_years',
            'mor_10_dp_interest',
            'mor_10_dp_principle_amt',
            'mor_10_dp_debt_amt',
            'mor_10_dp_monthly_pmt',
            'mor_10_dp_total_paid_amt',
            'mor_10_dp_total_interest',
            'mor_10_dp_down_pmt',
            'mor_10_dp_age_qualification',
            'mor_10_dp_pmt_qualification',
            'mor_10_dp_pmt',
            'mor_10_dp__of_supported_years',
            'mor_10_dp_monthly_support_and_principle',
            'mor_10_dp_support_and_interest',
            'mor_10_dp_full_interest_to_cover',
            'mor_10_dp_covered_interest',
            'mor_10_dp_monthly_support',
            'mor_10_dp_monthly_pmt_after_support',
            'mor_10_dp_total_paid_amt_after_support',
            'mor_15_dp_no_of_available_years',
            'mor_15_dp_interest',
            'mor_15_dp_principle_amt',
            'mor_15_dp_debt_amt',
            'mor_15_dp_monthly_pmt',
            'mor_15_dp_total_paid_amt',
            'mor_15_dp_total_interest',
            'mor_15_dp_down_pmt',
            'mor_15_dp_age_qualification',
            'mor_15_dp_pmt_qualification',
            'mor_15_dp_pmt',
            'mor_15_dp__of_supported_years',
            'mor_15_dp_monthly_support_and_principle',
            'mor_15_dp_support_and_interest',
            'mor_15_dp_full_interest_to_cover',
            'mor_15_dp_covered_interest',
            'mor_15_dp_monthly_support',
            'mor_15_dp_monthly_pmt_after_support',
            'mor_15_dp_total_paid_amt_after_support',
            'mor_20_dp_no_of_available_years',
            'mor_20_dp_interest',
            'mor_20_dp_principle_amt',
            'mor_20_dp_debt_amt',
            'mor_20_dp_monthly_pmt',
            'mor_20_dp_total_paid_amt',
            'mor_20_dp_total_interest',
            'mor_20_dp_down_pmt',
            'mor_20_dp_age_qualification',
            'mor_20_dp_pmt_qualification',
            'mor_20_dp_pmt',
            'mor_20_dp__of_supported_years',
            'mor_20_dp_monthly_support_and_principle',
            'mor_20_dp_support_and_interest',
            'mor_20_dp_full_interest_to_cover',
            'mor_20_dp_covered_interest',
            'mor_20_dp_monthly_support',
            'mor_20_dp_monthly_pmt_after_support',
            'mor_20_dp_total_paid_amt_after_support',
            'mor_25_dp_no_of_available_years',
            'mor_25_dp_interest',
            'mor_25_dp_principle_amt',
            'mor_25_dp_debt_amt',
            'mor_25_dp_monthly_pmt',
            'mor_25_dp_total_paid_amt',
            'mor_25_dp_total_interest',
            'mor_25_dp_down_pmt',
            'mor_25_dp_age_qualification',
            'mor_25_dp_pmt_qualification',
            'mor_25_dp_pmt',
            'mor_25_dp__of_supported_years',
            'mor_25_dp_monthly_support_and_principle',
            'mor_25_dp_support_and_interest',
            'mor_25_dp_full_interest_to_cover',
            'mor_25_dp_covered_interest',
            'mor_25_dp_monthly_support',
            'mor_25_dp_monthly_pmt_after_support',
            'mor_25_dp_total_paid_amt_after_support',
            'mor_max_dp_no_of_available_years',
            'mor_max_dp_interest',
            'mor_max_dp_principle_amt',
            'mor_max_dp_debt_amt',
            'mor_max_dp_monthly_pmt',
            'mor_max_dp_total_paid_amt',
            'mor_max_dp_total_interest',
            'mor_max_dp_down_pmt',
            'mor_max_dp_age_qualification',
            'mor_max_dp_pmt_qualification',
            'mor_max_dp_pmt',
            'mor_max_dp__of_supported_years',
            'mor_max_dp_monthly_support_and_principle',
            'mor_max_dp_support_and_interest',
            'mor_max_dp_full_interest_to_cover',
            'mor_max_dp_covered_interest',
            'mor_max_dp_monthly_support',
            'mor_max_dp_monthly_pmt_after_support',
            'mor_max_dp_total_paid_amt_after_support',
        ]

        return self.__dict_to_report({
            k : v
            for k,v in self.report_data.items()
            if k in pdf_output_columns
        })


    def get_other_dict(self):
        other_dict_columns = []
        other_dict_columns_prefix = [
            'debt_classification',
            'home_searching_status',
        ]
        for year in [10,15,20,25,'max']:
            prefix = f'mor_{year}_dp_'
            for col in other_dict_columns_prefix:
                other_dict_columns.append(prefix + col)

        return self.__dict_to_report({
            k : v
            for k,v in self.report_data.items()
            if k in other_dict_columns
        })