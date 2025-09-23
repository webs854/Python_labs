# Варіант - 5
# Завдання 3
n = int(input("Enter number: "))
while n < 1 or n > 9:
    n = int(input("Enter number again: "))

for i in range(1, n + 1):
    num = 5
    for j in range(i):
            print(num, end=" ")
            num -= 1
    print()
