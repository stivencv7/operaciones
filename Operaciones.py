# en esta funcion le estamos pidiendo al usuario q ingrese los numeros
def Ingresar_Numeros():
    try:
        numero1 = float(input("ingrese el primer numero: "))
        numero2 = float(input("ingrese el segundo numero: "))
        return numero1, numero2
    except Exception as e:
        print('Falta numeros : ')
        salir = str(input(
            "\n\tingrese 'si' si quiere seguir realizando operaciones | o presiona cualquier tecla para salir del programa:  "))

        if salir == 'si':
            menu()
        else:
            print('\t Programa terminado')
            print(exit())

# en esta funcion estamos sumando los numeros ingresados por el usuario


def suma(numero1, numero2):
    resultado = numero1+numero2
    return resultado

# en esta funcion estamos restando los numeros ingresados por el usuario


def resta(numero1, numero2):
    resultado = numero1-numero2
    return resultado

# en esta funcion estamos multiplicando los numeros ingresados por el usuario


def multiplicacion(numero1, numero2):
    resultado = numero1*numero2
    return resultado

# en esta funcion estamos dividiendo los numeros ingresados por el usuario


def divicion(numero1, numero2):
    try:
        numero2 != 0
        resultado = numero1/numero2
        return resultado
    except ZeroDivisionError as x:
        return 'error:', x, 'no se puede dividir por cero'


print()

# estse es el menu para reslizar una o todas las operaciones funcion


def menu():
    valor = Ingresar_Numeros()
    print()
    print("\t ingrese 1 para ver el resultado de la suma")
    print("\t ingrese 2 para ver el resultado de la resta")
    print("\t ingrese 3 para ver el resultado de la multiplicación")
    print("\t ingrese 4 para ver el resultado de la divición")
    print("\t ingrese 5 para ver el resultado de todas las operaciones")
    print()

    try:
        opcion = int(input("Favor ingresar la opcion de resultado:"))
    except Exception as e:
        print("la opción es erronia introduzca una opcion del 1 a 5 grasias")
        try:
            opcion = int(input("\nFavor ingresar la opcion de resultado:"))
        except Exception as e:
            print("error se reinicia el programa")
            print()
            menu()

    if opcion == 1:
        print("\n\t el resultado de la suma es: ",
              suma(valor[0], valor[1]))
    elif opcion == 2:
        print("\n\tel resultado de la resta es: ",
              resta(valor[0], valor[1]))
    elif opcion == 3:
        print("\n\tel resultado de la multiplicacion es: ",
              multiplicacion(valor[0], valor[1]))
    elif opcion == 4:
        print("\n\tel resultado de la divición es: ",
              divicion(valor[0], valor[1]))
    elif opcion == 5:
        print("\n\tel resultado de la suma es: ", suma(valor[0], valor[1]))
        print("\n\tel resultado de la resta es: ",
              resta(valor[0], valor[1]))
        print("\n\tel resultado de la multiplicacion es: ",
              multiplicacion(valor[0], valor[1]))
        print("\n\tel resultado de la divición es: ",
              divicion(valor[0], valor[1]))
    elif opcion == "":
        print("sintaxis no valida")
    else:
        print("error no concide la opción")

    salir = str(input(
        "\n\tingrese 'si' si quiere seguir realizando operaciones | o presiona cualquier tecla para salir del programa:  "))

    if salir == 'si':
        menu()

    else:
        print(exit())


menu()
