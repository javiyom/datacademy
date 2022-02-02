menu= """
Bienvenido al conversor de monedas


1 - Pesos Mexicanos.
2 - Pesos Colombianos.
3 - Pesos Argentinos.

Elige una opcion:  
"""
opcion = int(input(menu))

if opcion == 1:
    pesos = input ("cuantos pesos MEXICANOS tienes?:")
    pesos = float(pesos)
    valor_dolar = 20.58
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")
elif opcion == 2:
    pesos = input ("cuantos pesos COLOMBIANOS tienes?:")
    pesos = float(pesos)
    valor_dolar = 3,932.50
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")
elif opcion == 3:
    pesos = input ("cuantos pesos ARGENTINOS tienes?:")
    pesos = float(pesos)
    valor_dolar = 105.16
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("tienes $" + dolares + " dolares")
else:
    print('Solo hay 3 opciones, por favor elige una opcion disponible.')
    