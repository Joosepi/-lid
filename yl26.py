import pandas as pd

revenue = pd.DataFrame({
    'Johnver': [190,325,682,829],
    'Vanston': [140,19,14,140],
    'Danbree': [1926,293,852,609],
    'Vansey': [14,1491,56,120],
    'Mundyke': [143,162,659,87]
})

expenses = pd.DataFrame({
    'Johnver': [120,300,50,67],
    'Vanston': [65,10,299,254],
    'Danbree': [890,23,1290,89],
    'Vansey': [54,802,12,129],
    'Mundyke': [430,235,145,76]
})

total_revenue = revenue.subtract(expenses)

total_revenue[total_revenue < 0] = 0

commission = pd.DataFrame(columns=['Johnver', 'Vanston', 'Danbree', 'Vansey', 'Mundyke'])

for col in total_revenue:
    commission.loc["Commission", col] = round(sum(total_revenue[col] * .062))

print(commission)