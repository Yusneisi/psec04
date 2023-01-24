#Problem 1
lista1 = ["gatos", "", "perros", "ratones", ""]
lista1.pop(1)
lista1.pop(3)
print(lista1)

#Problem 2
lista1 = [1, 2, [200, 400, [1000, 6000], 800], 30, 40]
lista1[2][2].insert(1, 5000)
print(lista1)

#Problem 3
str1 = "Después de la tempestad, viene la calma"
str2 = str1[0] + str1[2] + str1[-1]
str2 = str2.lower()
print(str2)

#Problem 4
temperatura_centigrados = 20
c = temperatura_centigrados
temperatura_fahrenheit = (c * 9/5) + 32
temperatura_fahrenheit = round(temperatura_fahrenheit)
print(temperatura_fahrenheit)

#Problem 5
dict1 = {"Diez": 10, "Veinte": 20, "Treinta": 30}
dict2 = {"Treinta": 30, "Cuarenta": 40, "Cincuenta": 50}
dict1.update(dict2)
print(dict1)

#Problem 6
diccionarioEstudiante = {
    "clase": {
        "estudiante": {
            "nombre": "Mike", 
            "marcas": {
                "física": 70, 
                "historia": 80
            }
        }
    }
}
print(diccionarioEstudiante["clase"]["estudiante"]["marcas"].get("historia"))

#Problem 7
dict3 = {
    "nombre": "Platón", 
    "país": "Antigua Grecia", 
    "fecha de nacimiento": -427, 
    "maestro": "Sócrates", 
    "alumno": "Aristóteles"
}
dict3 ["fecha de nacimiento"] = -428
print(dict3)
