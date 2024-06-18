import os
CARGOS = ["CEO", "Desarrollador", "Analista de datos"]
DESC_SALUD = 70000
DESC_AFP = 120000


trabajadores = []


def registrar_trabajador():
    print("Registro de Trabajador")
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    cargo = ""
    while cargo not in CARGOS:
        print("Cargos disponibles:", CARGOS)
        cargo = input("Cargo: ")
    sueldo_bruto = int(input("Sueldo Bruto: "))
    
    
    descuento_total = DESC_SALUD + DESC_AFP
    liquido_pagar = sueldo_bruto - descuento_total
    
    
    trabajadores.append({
        'Nombre': nombre,
        'Apellido': apellido,
        'Cargo': cargo,
        'Sueldo Bruto': sueldo_bruto,
        'Desc. Salud': DESC_SALUD,
        'Desc. AFP': DESC_AFP,
        'Líquido a pagar': liquido_pagar
    })
    print("Trabajador registrado correctamente.\n")


def listar_trabajadores():
    print("\nLista de Trabajadores:")
    if not trabajadores:
        print("No hay trabajadores registrados.")
    else:
        for idx, trab in enumerate(trabajadores, start=1):
            print(f"{idx}. {trab['Nombre']} {trab['Apellido']}, Cargo: {trab['Cargo']}, Sueldo Bruto: {trab['Sueldo Bruto']}, Líquido a pagar: {trab['Líquido a pagar']}")
    print() 


def imprimir_planilla():
    print("\nImprimir Planilla de Sueldos")
    if not trabajadores:
        print("No hay trabajadores registrados para imprimir la planilla.")
        return
    
    print("Cargos disponibles:", CARGOS)
    cargo_seleccionado = input("Seleccione un cargo para generar la planilla (o 'todos' para imprimir todos): ")
    
    if cargo_seleccionado.lower() == 'todos':
        trabajadores_a_imprimir = trabajadores
        nombre_archivo = "planilla_todos.txt"
    elif cargo_seleccionado in CARGOS:
        trabajadores_a_imprimir = [trab for trab in trabajadores if trab['Cargo'] == cargo_seleccionado]
        nombre_archivo = f"planilla_{cargo_seleccionado.lower().replace(' ', '_')}.txt"
    else:
        print(f"Cargo '{cargo_seleccionado}' no válido.")
        return
    
    with open(nombre_archivo, 'w') as archivo:
        archivo.write("Planilla de Sueldos\n")
        archivo.write("==================\n\n")
        for trab in trabajadores_a_imprimir:
            archivo.write(f"Nombre: {trab['Nombre']} {trab['Apellido']}\n")
            archivo.write(f"Cargo: {trab['Cargo']}\n")
            archivo.write(f"Sueldo Bruto: {trab['Sueldo Bruto']}\n")
            archivo.write(f"Desc. Salud: {trab['Desc. Salud']}\n")
            archivo.write(f"Desc. AFP: {trab['Desc. AFP']}\n")
            archivo.write(f"Líquido a pagar: {trab['Líquido a pagar']}\n\n")
    
    print(f"Se ha generado el archivo '{nombre_archivo}' correctamente.\n")


def main():
    while True:
        print("Menú Principal")
        print("1. Registrar Trabajador")
        print("2. Listar Trabajadores")
        print("3. Imprimir Planilla de Sueldos")
        print("4. Salir del Programa")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            registrar_trabajador()
        elif opcion == '2':
            listar_trabajadores()
        elif opcion == '3':
            imprimir_planilla()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.\n")

if __name__ == "__main__":
    main()
