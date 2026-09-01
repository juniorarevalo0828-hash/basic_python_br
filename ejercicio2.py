numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

print("Suma:", numero1 + numero2)
print("Resta:", numero1 - numero2)
print("Multiplicación:", numero1 * numero2)

if numero2 != 0:
    print("División:", numero1 / numero2)
    print("División entera:", numero1 // numero2)
    print("Módulo:", numero1 % numero2)
else:
    print("No se puede dividir entre cero")

print("Potencia:", numero1 ** numero2)
