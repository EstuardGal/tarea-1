num1=int(input("Ingrese un numero entero:"));
num2=int(input("Ingrese otro numero:"));
num3=int(input("Ingrese otro numero:"));
if num1>num2 and num1>num3:
    print("El numero mayor es:",num1);
elif num2>num1 and num2>num3:
    print("El numero mayor es:",num2);
else:
    print("El numero mayor es:",num3);

