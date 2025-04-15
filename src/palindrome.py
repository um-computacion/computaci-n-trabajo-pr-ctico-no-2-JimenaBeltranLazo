#FASE 2: Implementacion de la Solución "Detector Palíndromos"

def is_palindrome(word_phrase: str) -> bool:
    #Ignorar Mayúsculas (convertir a minúsculas)
    word_phrase = word_phrase.lower()
    #Ignorar Acentos
    word_phrase = word_phrase.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
    #Leer Número como Carácter
    cleaned_word_phrase = ''.join(char for char in word_phrase if char.isalnum())

    return cleaned_word_phrase == cleaned_word_phrase[::-1]

my_word_phrase = input("Bienvenido al Deterctor de Palíndromos. Ingrese un palabra o frase: ")
if is_palindrome(my_word_phrase):
    print(f"{my_word_phrase} es un palíndromo.")
else:
    print(f"{my_word_phrase} no es un palíndromo.")