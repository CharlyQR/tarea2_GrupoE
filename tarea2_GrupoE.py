import math


def main():
    print("Tarea #2 de un programa de cálculo de fuerza neta y aceleración")
    

def ingresarFuerzas():
    fuerzas = []
    cantidadFuerzas = int(input("Ingrese la cantidad de fuerzas a calcular: "))

    for i in range(cantidadFuerzas):
        print(f"\nFuerza #{i + 1}")
        metodoIngreso = input(
            "¿Cómo desea ingresar esta fuerza?" \
            "\n1. Magnitud y dirección" \
            "\n2. Componentes Fx y Fy" \
            "\nSeleccione una opción: ")
        
        if metodoIngreso == 1:
            magnitudFuerza = float(input("Ingrese la magnitud de la Fuerza N: "))
            anguloFuerza = float(input("Ingrese el ángulo de la Fuerza en grados: "))
            anguloRadianes = math.radians(anguloFuerza)
            fx = magnitudFuerza * math.cos(anguloRadianes)
            fy = magnitudFuerza * math.sin(anguloRadianes)
        elif metodoIngreso == 2:
            fx = float(input("Ingrese el componente Fx de la Fuerza N: "))
            fy = float(input("Ingrese el componente Fy de la Fuerza N: "))
        else:
            print("Datos inválidos")
            continue

    fuerzas.append((fx, fy))

    return fuerzas

if __name__ == "__main__":
    main()