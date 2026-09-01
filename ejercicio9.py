try:
    numero1 = float(input("Ingrese el primer número: "))
    numero2 = float(input("Ingrese el segundo número: "))

    resultado = numero1 / numero2

    print("El resultado de la división es:", resultado)

except ZeroDivisionError:
    print("Error: No se puede dividir entre cero.")

except ValueError:
    print("Error: Debe ingresar números válidos.")
