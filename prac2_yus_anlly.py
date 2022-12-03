print("Bienvenido\n")

print("----------------------------------------------------------")
operador = input("Ingrese la operación que desea realizar (+, - *, /): ")
print("----------------------------------------------------------")

if operador == "/" :
    dividendo = int(input("Ingrese el número que desea dividir: "))
    divisor = int(input("Ingrese el número por el cual desea dividir: "))
    if divisor == 0 :
        divisor2 = int(input("No juegues conmigo, ingresa otro número: "))
        print(dividendo / divisor2)
    else :
        print(dividendo / divisor)
elif operador == "+" :
    valor1 = int(input("Ingrese un número: "))
    valor2 = int(input("Ingrese otro número: "))
    print(valor1 + valor2)
elif operador == "-" :
    valor1 = int(input("Ingrese un número: "))
    valor2 = int(input("Ingrese otro número: "))
    print(valor1 - valor2)
elif operador == "*" :
    valor1 = int(input("Ingrese un número: "))
    valor2 = int(input("Ingrese otro número: "))
    print(valor1 * valor2)
else :
    print("Solo ingrese las operaciones antes mencionadas")
