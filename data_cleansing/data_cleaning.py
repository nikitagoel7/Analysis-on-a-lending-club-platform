# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 13:46:50 2022

@author: Nikita Goel
"""

import pandas as pd
main_df = pd.read_csv('loans_full_schema.csv')
ir = main_df["interest_rate"].tolist()
annual_income = ["1:" + str(i) for i in main_df["annual_income"].tolist()]
credit_limit = ["2:" + str(i) for i in main_df["total_credit_limit"].tolist()]
debit_limit = ["3:" + str(i) for i in main_df["total_debit_limit"].tolist()]
loan_amount = ["4:" + str(i) for i in main_df["loan_amount"].tolist()]
term = ["5:" + str(i) for i in main_df["term"].tolist()]
installment = ["6:" + str(i) for i in main_df["installment"].tolist()]
interest_rate = ["7:" + str(i) for i in main_df["interest_rate"].tolist()]
res = []
for i in range(len(ir)):
    st = str(ir[i]) +' ' + str(annual_income[i]) +' '+ str(credit_limit[i]) +' '+ str(debit_limit[i]) +' '+ str(loan_amount[i]) +' '+ str(term[i]) +' '+ str(installment[i]) +' '+ str(interest_rate[i])
    res.append(st)

writer = open('interest_rate_feature_set.txt', 'w')
for i in res:
    writer.write(i + '\n')

writer.close()