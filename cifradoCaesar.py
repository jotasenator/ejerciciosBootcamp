
# para cambiar de colores .reseteo + color + reseteo
from colorama import Style, Fore

# cifrado tipo Caesar n

cifrado = int(input('Teclee de cuantos numeros desea el cifrado: '))

clave = input('Teclee una palabra: ')

palabra_final = [chr(ord(palabra)+cifrado) for palabra in clave]


print(
    f'esto sustituye letra por letra de la palabra {Style.RESET_ALL+ Fore.RED + clave + Style.RESET_ALL} en las proximas {cifrado} posiciones -->', Style.RESET_ALL + Fore.BLUE + ''.join(palabra_final) + Style.RESET_ALL)  # + Style.BRIGHT


# ahora hacemos el cifrado

clave = input('Teclee la palabra secreta: ')

cifrado = int(input('Teclee de cuantos numeros fue el cifrado: '))

palabra_inicial = [chr(ord(elemento) - cifrado) for elemento in clave]

print(
    f'esto sustituye letra por letra de la palabra secreta {Style.RESET_ALL + Fore.BLUE + clave + Style.RESET_ALL} en las pasadas {cifrado} posiciones -->', Style.RESET_ALL + Fore.RED + ''.join(palabra_inicial) + Style.RESET_ALL)
