def es_numero_perfecto(numero):
    if numero <= 0:
        return False

    suma_divisores = 0

    for i in range(1, numero):
        if numero % i == 0:
            suma_divisores += i

    if suma_divisores == numero:
        return True
    else:
        return False


test_numbers = [6, 28, 496, 12]

for n in test_numbers:
    if es_numero_perfecto(n):
        print(f" {n} es un número perfecto.")
    else:
        print(f" {n} no es un número perfecto.")