for row in range(1, 11):
    for col in range(1, 11):
        symbol = col * row
        print(symbol, "\t", end = '')
    print()

Здравствуйте!
Вопрос по уроку 14.3  "Командная строка и интерпретатор".
Непонятно, почему не выполняется в командной строке команда "python [имя файла]" (интерпретатор установлен). 
Непонятно, как в интерпретаторе ввести программу длиной более одной строки. 

Задача 2. Калькулятор

Напишите программу калькулятор. Пользователь вводит два числа A и B и действие X (плюс, минус, умножить, разделить). 
Программа выводит результат в виде A X B = C, где C — результат этого действия над числами A и B. 
Используйте только консоль и текстовый редактор. Обеспечьте контроль ввода.


Пример работы программы в консоли:

Выберите операцию: +

Введите первое число: 5

Введите второе число: 6

5 + 6 = 11


def operation(number_a, operator, number_b):
    result = number_a operator number_b
    print(result)
operation = input("Выберите операцию: ")
number_1 = float(input("Введите первое число: "))
number_2 = float(input("Введите второе число: "))
operation(number_a, operator, number_b)



operation = input("Выберите операцию: ")
number_1 = float(input("Введите первое число: "))
number_2 = float(input("Введите второе число: "))
if operation == "+":
    result = number_1 + number_2
elif operation == "-":
    result = number_1 - number_2
elif operation == "*":
    result = number_1 * number_2
else:
    result = number_1 / number_2
print(result)
 