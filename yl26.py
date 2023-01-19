import pandas as pd

revenue = pd.DataFrame({
    'Chase': [190,325,682,829],
    'Babylee': [140,19,14,140],
    'Daniel': [1926,293,852,609],
    'Valerina': [14,1491,56,120],
    'Monkey': [143,162,659,87]
})

expenses = pd.DataFrame({
    'Chase': [120,300,50,67],
    'Babylee': [65,10,299,254],
    'Daniel': [890,23,1290,89],
    'Valerina': [54,802,12,129],
    'Monkey': [430,235,145,76]
})

total_revenue = revenue.subtract(expenses)

total_revenue[total_revenue < 0] = 0

commission = pd.DataFrame(columns=['Chase', 'Babylee', 'Daniel', 'Valerina', 'Monkey'])

for col in total_revenue:
    commission.loc["Commission", col] = round(sum(total_revenue[col] * .062))

print(commission)