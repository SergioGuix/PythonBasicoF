print("Indice de masa corporal")

peso = float(input("Ingrese su peso en kg "))
altura = float(input("Ingrese su altura en m "))

imc = round((peso / (altura**2)),2)

print('Tu indice de masa corporal es ' , imc )