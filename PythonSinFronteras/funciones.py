import random

def maximum(value1, value2, value3):
    """Evalua el mayor de tres valores"""
    max_value = value1
    if value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

def imprimir(valor):
    print(f'El valor es:{valor:>10}')

def estudiantes(*name): #Almacena los valores ingresados en tuplas
    total = name
    total = set(total)
    print(total, type(total))

def personal(**kwrargs): #Realiza el ingreso de argumentos tipo diccionario
    for i in kwrargs:
        print(kwrargs[i])

#personal(docente='Cristhial laureano', dni='70104505', code_postal=21001)

def alumnos(*arg, **kwrargs):
     print(arg, kwrargs)

#alumnos('cristhia', 'diana', 'olga', 'franciso', materias='matematica', horario='morning', time='6')

def factorial(number):
    if number == 1:
        return 1
    else:
        return number * factorial(number-1)

def fibonaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonaci(n-1) + fibonaci(n-2)

print(fibonaci(7))


    