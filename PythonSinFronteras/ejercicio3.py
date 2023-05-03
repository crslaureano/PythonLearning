# Ejercicio de Calculadora
try:
    number1 = int(input('Valor 1: '))
except:
    print('Solo Numeros')
    exit()
try:
    number2 = int(input('Valor 2: '))
except:
    print('Solo Numeros')
    exit()

operation = input('que operacion quiere realizar +-*/')
if operation == '+':
    print(number1+number2)
elif operation == '-':
    print(number1-number2)
elif operation == '*':
    print(number1*number2)
elif operation == '/':
    print(number1/number2)
else:
    print('No se encontro la operacion')
