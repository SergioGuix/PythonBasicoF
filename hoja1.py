#ejercicio  < 
print(" ---------------- Ejercicio 1 -------------------")

num2 = int(input("Ingrese un numero positivo "))
contador = 0
letra = "*"

while contador  < num2:
    
    print(letra)
    letra = letra + "*"
    contador = contador + 1

    



    #ejercicio 2
  
print("--------------- Ejercicio 2 -----------------")

num3 = int(input("Ingrese un numero positivo "))



for i in range(-1, num3):
    
    print(num3)
    num3-=1
 
print("----------- Ejercicio 3 --------------------") 
num4 = int(input("Ingrese un numero para verificar si es impar "))

if num4 % 2 :
    print(" El numero " , num4 , " es numero primo ")
    
else:
    print(" El numero " , nume4 , " es numero par ")