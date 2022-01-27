pesos = input ("cuantos pesos mexicanos tienes?:")
pesos = float(pesos)
valor_dolar = 20.30
dolares = pesos / valor_dolar
dolares = round(dolares, 2)
dolares = str(dolares)
print("tienes $" + dolares + " dolares")
