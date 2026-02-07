def es_vocal(caracter):
    vocales_referencia = "aeiouáéíóú"

    if len(caracter) != 1:
        return "Error: Por favor, ingresa solo un carácter."

    if caracter.lower() in vocales_referencia:
        return True
    else:
        return False


entrada = input("Introduce un carácter para el análisis NLP: ")
resultado = es_vocal(entrada)

if resultado is True:
    print(f"🎯 Patrón Detectado: '{entrada}' es una vocal.")
elif resultado is False:
    print(f"🔍 Patrón No Detectado: '{entrada}' es una consonante o símbolo.")
else:
    print(resultado)