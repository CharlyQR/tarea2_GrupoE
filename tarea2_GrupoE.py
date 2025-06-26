import math
import matplotlib.pyplot as plot

def main():
    print("Tarea #2 de un programa de cálculo de fuerza neta y aceleración")

    fuerzas = ingresarFuerzas()

    print("\nFuerzas ingresadas:")
    for i, (fx, fy) in enumerate(fuerzas):
        print(f"Fuerza #{i + 1}: Fx = {fx:.2f} N, Fy = {fy:.2f} N")

    fxTotal, fyTotal, fuerzaMagnitud = calcularFuerzaNeta(fuerzas)

    masa = float(input("\nIngrese la masa del bloque en kilogramos: "))
    aceleracionX, aceleracionY, magnitudAceleracion = calcularAceleracion(fxTotal, fyTotal, masa)

    print("\n-----Fuerzas Neta-----")
    print(f"Fuerza FX Total: {fxTotal:.2f} N")
    print(f"Fuerza FY Total: {fyTotal:.2f} N")
    print(f"Magnitud total: {fuerzaMagnitud:.2f} N")

    print("\n-----Aceleración-----")
    print(f"Aceleración en X: {aceleracionX:.2f} m/s²")
    print(f"Aceleración en Y: {aceleracionY:.2f} m/s²")
    print(f"Magnitud de la aceleración: {magnitudAceleracion:.2f} m/s²")

    graficarFuerzas(fuerzas, fxTotal, fyTotal)
    

def ingresarFuerzas():
    fuerzas = []
    cantidadFuerzas = int(input("Ingrese la cantidad de fuerzas a calcular: "))

    for i in range(cantidadFuerzas):
        print(f"\nFuerza #{i + 1}")
        
        while True:
            metodoIngreso = input(
                "¿Cómo desea ingresar esta fuerza?"
                "\n1. Magnitud y dirección"
                "\n2. Componentes Fx y Fy"
                "\nSeleccione una opción: ")

            if metodoIngreso == "1":
                magnitudFuerza = float(input("Ingrese la magnitud de la Fuerza N: "))
                anguloFuerza = float(input("Ingrese el ángulo de la Fuerza en grados: "))
                anguloRadianes = math.radians(anguloFuerza)
                fx = magnitudFuerza * math.cos(anguloRadianes)
                fy = magnitudFuerza * math.sin(anguloRadianes)
                break
            elif metodoIngreso == "2":
                fx = float(input("Ingrese el componente Fx de la Fuerza N: "))
                fy = float(input("Ingrese el componente Fy de la Fuerza N: "))
                break
            else:
                print("Opción inválida. Por favor seleccione 1 o 2.")

        fuerzas.append((fx, fy))

    return fuerzas



def calcularFuerzaNeta(fuerzas):
    sumaFX = sum(fx for fx, _ in fuerzas)
    sumaFY = sum(fy for _, fy in fuerzas)
    magnitudFuerza = math.sqrt(sumaFX**2 + sumaFY**2)
    return (sumaFX, sumaFY, magnitudFuerza)


def calcularAceleracion(fxTotal, fyTotal, masa):
    aceleracionX = fxTotal / masa
    aceleracionY = fyTotal / masa
    magnitudAceleracion = math.sqrt(aceleracionX**2 + aceleracionY**2)
    return (aceleracionX, aceleracionY, magnitudAceleracion)

def graficarFuerzas(fuerzas, fxNeta, fyNeta):
    plot.figure()
    plot.axhline(0, color='black', linewidth=0.5)
    plot.axvline(0, color='black', linewidth=0.5)

    plot.plot(0, 0, 'ks', markersize=10, label='Bloque')

    for i, (fx, fy) in enumerate(fuerzas):
        plot.arrow(0, 0, fx, fy, head_width=0.2, length_includes_head=True, label=f'Fuerza #{i + 1}')

    plot.arrow(0,0, fxNeta, fyNeta, head_width=0.3, color='red', length_includes_head=True, label='Fuerza Neta')

    plot.xlabel("Eje X (N)")
    plot.ylabel("Eje Y (N)")
    plot.grid(True)
    plot.legend()
    plot.axis('equal')
    plot.title("Diagrama de Fuerzas")
    plot.show()


if __name__ == "__main__":
    main()