num1=int(input("Ingrese un numero:"));
num2=int(input("Ingrese otro numero:"));
num3=int(input("Ingrese el tercer numero:"));
total=num1+num2+num3
if total % 7==0:
    print("El numero", total, "es multiplo de 7")
else:
    print("El numero", total, "no es multiplo de 7")