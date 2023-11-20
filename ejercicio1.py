num1=int(input("Ingrese un numero entero:"));
num2=int(input("Ingrese otro numero"));
if num1>num2:
    mensaje="El numero",num1 ,"es mayor"
    mensaje1="El numero",num2 ,"es menor"

elif num1==num2:
    mensaje="Los numeros son iguales"
else:
    mensaje="El numero" ,num1,"es menor"
    mensaje1 = "El numero", num2, "es mayor"
print(mensaje)
print(mensaje1)