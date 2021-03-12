#-------------- Ejercicio 1 --------------------
contraseña = input("Ingrese una contraseña")

contraseña2 = input("Ingrese la contraseña de nuevo para verificar")

#.strip para ignorar espacios en blanco <>
if contraseña.lower() == contraseña2.lower():
    print("Se ha verificado que la contraseña es correcta")

else:
        print("Contraseña incorrecta")
        
#------------------- Ejercicio -------------------------
#Masculino 
#Femenino
nombre = input("Ingrese su nombre")
sexo = input("Ingrese su sexo M O F")
M = "M"
F = "F"
N = "N"

if sexo.upper() == F:
    if nombre.upper() < M:       
        grupo = "A"
    else:
        grupo = "B"   
else:
    if sexo.upper() == M: 
        if nombre.upper() > N:
            grupo = "A"   
        else:
            grupo = "B"
    else:
            grupo = "B" 
    
print(nombre , " pertenece al grupo " , grupo)


