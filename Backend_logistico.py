def calcular_costo_transporte():
    print("--- Sistema de Cálculo de Transportes ---")
    print("Opciones de vehículo: Pickup, Gandola, Mudanza")

    vehiculo = input("Seleccione el tipo de vehículo: ").strip().capitalize()

    try:
        distancia = float(input("Ingrese la distancia a recorrer (km): "))

        tasa_km = 1.50
        precio_base = 0.0

        match vehiculo:
            case "Pickup":
                precio_base = 6.00
            case "Gandola":
                precio_base = 7.00
            case "Mudanza":
                precio_base = 10.00
            case _:
                print("Error: Vehículo no reconocido.")
                return

        costo_distancia = distancia * tasa_km
        monto_total = precio_base + costo_distancia

        # 4. Reporte final desglosado
        print("\n" + "=" * 30)
        print("REPORTE DE FACTURACIÓN")
        print("=" * 30)
        print(f"Vehículo seleccionado: {vehiculo}")
        print(f"Distancia:            {distancia:.2f} km")
        print(f"Precio Base:         ${precio_base:.2f}")
        print(f"Costo por Distancia: ${costo_distancia:.2f}")
        print("-" * 30)
        print(f"TOTAL A PAGAR:       ${monto_total:.2f}")
        print("=" * 30)

    except ValueError:
        print("Error: La distancia debe ser un número (ejemplo: 10.5).")


if __name__ == "__main__":
    calcular_costo_transporte()