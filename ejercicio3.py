numero = int(input("Ingrese un número entero: "))

if numero % 2 == 0:
    print("El número es par")
else:
    siguiente_par = numero + 1
    print("El número es impar")
    print("El siguiente número par es:", siguiente_par)
