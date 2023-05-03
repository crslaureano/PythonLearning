# try:
    # number1 = int(input('number 1: '))
    # number2 = int(input('number 2: '))
    # print(f'La suma es {number1 + number2}')
# except:
    # print('Solo numeros')

number1 = input('Number 1: ')
try:
    number1 = int(number1)
except:
    number1 = 'ChanchitoFeliz'
if number1 == 'ChanchitoFeliz':
    print('Valor ingresado no es un entero')
    exit() # ara que nuestro programa salga de la ejecucion

number2 = input('Number 2: ')
try:
    number2 = int(number2)
except:
    number2 = 'ChanchitoFeliz'
if number2 == 'ChanchitoFeliz':
    print('Valor ingresado no es un entero')
    exit() #ara que nuestro programa salga de la ejecucion

print(number1 + number2)
