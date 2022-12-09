#First problem
number_1 = 0
print(number_1)
while number_1 < 9:
    number_1 += 1
    print(number_1)

#Second problem
string_integer = input("Ingrese un número entero: ")
try:
    if string_integer.isnumeric():
        number_2 = int(string_integer)
    print("El número ingresado es: ", number_2)
except:
    print("¡ERROR! El valor ingresado no es un número entero")
    while not string_integer.isnumeric():
        string_integer = input("Intente de nuevo: ")
    number_2 = int(string_integer)
    print("El número ingresado es: ", number_2)

list_numbers = [number_2]
while number_2 > 1:
    number_2 -= 1
    list_numbers.append(number_2)
print("La suma es: ", sum(list_numbers))
