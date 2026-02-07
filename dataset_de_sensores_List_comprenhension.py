datos_celsius = [20.5, 25.0, 30.2, 15.8, 10.0]

datos_fahrenheit = [(c * 9/5) + 32 for c in datos_celsius]

print(f"Original (Celsius):    {datos_celsius}")
print(f"Convertido (Fahrenheit): {datos_fahrenheit}")