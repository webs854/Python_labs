# Варіант-17
# Завдання 2
#"Щомісячна стипендія студена складає 50 грн., а загальні витрати на місяць 80 грн., визначте, яку суму студент візьме в борг за 10 міс., якщо загальні витрати зростають на 2% кожного місяця."

stipend = 50
expenses = 80
debt = 0

print("Month  |Expenses    |Difference |Debt  ")

for month in range(1, 11):
    difference = expenses - stipend
    debt += difference
    expenses *= 1.02
    print(f"{month:6} | {expenses:10.2f} | {difference:9.2f} | {debt:9.2f}")
