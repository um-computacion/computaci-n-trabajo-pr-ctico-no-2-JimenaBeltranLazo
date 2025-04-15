def is_palindrome(word_phrase: str) -> bool:
    #Ignorar Mayúsculas (convertir a minúsculas)
    word_phrase = word_phrase.lower()
    #Ignorar Acentos
    word_phrase = word_phrase.replace("á", "a").replace("é", "e").replace("í", "i").replace("ó", "o").replace("ú", "u")
    #Leer número como carácter
    cleaned_word_phrase = ''.join(char for char in word_phrase if char.isalnum())

    return cleaned_word_phrase == cleaned_word_phrase[::-1]
