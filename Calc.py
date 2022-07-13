operation = input("\nВыберите операцию: ")
ops = ["+", "-", "*", "/"]

while operation not in ops:
    operation = input('Ошибка: такой операции не существует. Попробуйте ещё раз.')

opsQuant = int(input("Количество операндов: "))
result = float(input('Введите операнд 1: '))
text = str(result)

for opNumber in range(2, opsQuant + 1):
    operand = float(input(f'Введите операнд {opNumber}: '))
    text += f' {operation} {operand}'
    if operation == "+":
        result += operand
    elif operation == "-":
        result -= operand
    elif operation == "*":
        result *= operand
    else:
        result /= operand

print(f'\n{text} = {result}')