# Mortgage_rm

- Calculation of mortgage

# Folder Structure

| Script                             | Description                                                         |
| ---------------------------------- | ------------------------------------------------------------------- |
| mortgage_calculations.ipynb        | Main calculation script, to calculate & produce output as json.     |
| craftmypdf_api.ipynb               | To send request & get pdf file from `craftmypdf` .                  |
| formula_extract.ipynb              | To extract `output/formula.csv` for streamlit dashboard purpose.    |
| dashboard/main.py                  | To use the mortgage UI calculator, depends on `output/formula.csv`. |
| dashboard/main.yml                 | To control what inputs/output shows in streamlit dashboard.         |
| mortgage_formular.py<br />utils.py | Helper scripts                                                      |

# Appendix

## Shortcut

1. Mor - Mortgage
2. Aff - Affordabilty
3. DB - Down Payment
4. ndp - No doawn payment
5. Aff_Max_DP Max Debt AMT - Aff home price
6. pv - present value
7. pmt - payment
8. Upfront costs - the costs you pay out of pocket once your offer on a home has been accepted
9. Down Payment - the initial payment that's made towards the purchase price of your home and is a cost that is made out-of-pocket
