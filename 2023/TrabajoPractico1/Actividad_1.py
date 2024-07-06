# Dado un número, mostrar si es:
# • Cero, mayor o menor que cero.
# • Par o impar (cuando sea mayor que cero)
# • Múltiplo de 8 o no múltiplo de 8 (cuando sea par).
# Por ejemplo: para el número 24, deberá mostrarse
#    Es un número mayor que cero.
#    Es par.
#    Es múltiplo de 8.

# Se ingresa un número de tipo entero
numero = int(input("Ingrese un número: "))

if numero > 0:
    print("Es un número mayor que cero.")
    # La siguiente expresión es el resto de la división de la varible "numero" entre 2.
    if numero % 2 == 0:
        print("Es par.")
        aux = (numero // 8) * 8 # Esta expresión es igual a: int(numero/8)*8
        if numero == aux:
            print("Es múltiplo de 8.")
        else:
            print("No es múltiplo de 8.")
    else:
        print("Es impar.")
else:
    if numero == 0:
        print("Es un número igual que cero.")
    else:
        print("Es un número menor que cero.")

# AHORA RESOLVEMOS USANDO ELIF
# if numero > 0:
#     print("Es un número mayor que cero.")
#     if numero % 2 == 0:
#         print("Es par.")
#         aux = (numero // 8) * 8
#         if numero == aux:
#             print("Es múltiplo de 8.")
#         else:
#             print("No es múltiplo de 8.")
#     else:
#         print("Es impar.")
# elif numero == 0:
#     print("Es un número igual que cero.")
# else:
#     print("Es un número menor que cero.")