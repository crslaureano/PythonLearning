# el usuario ingresa un dato y trata de adivinar si existe en la lista

dato = input('Ingrese dato: ')
lista = ['Hola', 'Mundo', 'Peluza', 'dragron']

if lista.count(dato) > 0:
    print('lolograste!')
else:
    print('No lolograste!')
