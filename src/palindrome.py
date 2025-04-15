import re



def is_palindrome(palabra):
    texto_limpio = limpiar_texto(palabra)
    return texto_limpio == texto_limpio[::-1]

if __name__ == "__main__":
    ''''''
    