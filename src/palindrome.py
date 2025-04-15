import re

def limpiar_texto(texto):
    return re.sub(r'[^\w]', '', texto.lower())

def is_palindrome(palabra):
    texto_limpio = limpiar_texto(palabra)
    return texto_limpio == texto_limpio[::-1]

if __name__ == "__main__":
    try:
        while True:
            print("Presione Control+c para finalizar")
            palabra = input("Ingrese una palabra o frase:  ")
            if is_palindrome(palabra):
                print(f"{palabra} es un palíndromo")
            else:
                print(f"{palabra} no es un palíndromo")
    except KeyboardInterrupt:
        print("\nPrograma finalizado por el usuario")