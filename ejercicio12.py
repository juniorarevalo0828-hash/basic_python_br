def comparar_numeros(a, b):

    if a > b:
        print(a, "es mayor que", b)

    elif b > a:
        print(b, "es mayor que", a)

    else:
        print("Ambos números son iguales")


numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

comparar_numeros(numero1, numero2)
