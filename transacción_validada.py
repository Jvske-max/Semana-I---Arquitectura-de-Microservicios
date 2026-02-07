def validar_transaccion():
    print("--- Sistema de Validación de Pagos ---")

    metodo = input("Ingrese el método de pago (Pago Movil / Tarjeta): ").strip().lower()

    clave = input("Ingrese su clave o número de validación: ").strip()

    if metodo == "pago movil":
        if clave.isdigit() and len(clave) == 8:
            print("Éxito: Pago Móvil validado correctamente.")
        else:
            print("Error: El Pago Móvil debe contener exactamente 8 números.")

    elif metodo == "tarjeta":
        if clave.isdigit() and len(clave) == 16:
            print("Éxito: Tarjeta validada correctamente.")
        else:
            print("Error: La Tarjeta debe contener exactamente 16 números.")

    else:
        print("Error: Método de pago no reconocido.")


validar_transaccion()