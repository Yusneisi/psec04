#First problem
word_1 = input("Ingrese una palabra: ")
word_2 = input("Ingrese otra palabra: ")

message_tuple = (
    "Las palabras ingresadas no peden ser anagramas; dado que no "
    "tienen el mismo número de caracteres", 
    "Intente una vez más, ingrese una palabra: ",
    "Ingrese otra palabra: ",
    "La primera palabra ingresada debe contener solo letras",
    "La segunda palabra ingresada solo debe contener letras",  
    "Las palabras \"{}\" y \"{}\" son anagramas",
    "Las palabras \"{}\" y \"{}\" no son anagramas",
    "Se terminaron sus intentos, vuelva cuando este seguro de lo "
    "que realmente desea hacer."
)

attempts = 3
try:
    if len(word_1) == len(word_2) and word_1.isalpha() and \
        word_2.isalpha:
        pass
    else:
        raise ValueError("")
except ValueError:
    while attempts > 0:
        if len(word_1) != len(word_2):
            attempts -= 1
            print(message_tuple[0])
            word_1 = input(message_tuple[1])
            word_2 = input(message_tuple[2])
        elif not (word_1.isalpha()):
            print(message_tuple[3])
            attempts -= 1
            word_1 = input("Intente de nuevo: ")
        elif not word_2.isalpha():
            print(message_tuple[4])
            attempts -= 1
            word_2 = input("Intente de nuevo: ")
        else:
            break

if attempts > 0:
    word_1.lower()
    word_2.lower()
    word_1_list = list(word_1)
    word_2_list = list(word_2)
    word_1_list.sort()
    word_2_list.sort()
    ordinate_word_1 = "".join(word_1_list)
    ordinate_word_2 = "".join(word_2_list)
    if ordinate_word_1 == ordinate_word_2:
        print(message_tuple[5].format(word_1, word_2))
    else:
        print(message_tuple[6].format(word_1, word_2))
else:
    print(message_tuple[7])

#Second problem
sentence_string = input("Ingrese una oración: ")
sentence_list = sentence_string.split()

number_of_validations = len(sentence_list)
for only_alphabets in sentence_list:
    if not only_alphabets.isalpha():
        number_of_validations -= 1

if number_of_validations != len(sentence_list):
    print(
        "La oracion ingresada, \"{}\", solo debe contener letras. "
        "Intente más tarde.".format(sentence_string)
    )
else:
    sentence_string = sentence_string.lower()
    initial_letter = sentence_list[0][0]

    repetitions = 0
    for first_letter in sentence_list:
        if first_letter[0] == initial_letter:
            repetitions += 1

    if repetitions == len(sentence_list):
        print("True")
    else:
        print("False")