import csv
import os

archivo_csv = 'datoseje2.csv'

def inicializar_archivo():
    if not os.path.isfile(archivo_csv):
        with open(archivo_csv, mode='w', newline='') as file:
            escritor = csv.writer(file)
            escritor.writerow(["Nombre", "Correo", "Teléfono"])

def agregar_contacto():
    nombre = input("Ingrese el nombre: ")
    correo = input("Ingrese el correo: ")
    telefono = input("Ingrese el teléfono: ")

    with open(archivo_csv, mode='a', newline='') as file:
        escritor = csv.writer(file)
        escritor.writerow([nombre, correo, telefono])

    print("Contacto agregado exitosamente.")

def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    contactos = []

    with open(archivo_csv, mode='r', newline='') as file:
        lector = csv.reader(file)
        contactos = [linea for linea in lector if linea[0] != nombre]

    with open(archivo_csv, mode='w', newline='') as file:
        escritor = csv.writer(file)
        escritor.writerows(contactos)

    print("Contacto eliminado exitosamente.")

def buscar_contacto():
    nombre = input("Ingrese el nombre del contacto a buscar: ")

    with open(archivo_csv, mode='r', newline='') as file:
        lector = csv.reader(file)
        for linea in lector:
            if linea[0] == nombre:
                print(f"Nombre: {linea[0]}, Correo: {linea[1]}, Teléfono: {linea[2]}")
                return

    print("Contacto no encontrado.")

def listar_contactos():
    with open(archivo_csv, mode='r', newline='') as file:
        lector = csv.reader(file)
        for linea in lector:
            print(f"Nombre: {linea[0]}, Correo: {linea[1]}, Teléfono: {linea[2]}")

def mostrar_menu():
    print("1. Agregar contacto")
    print("2. Eliminar contacto")
    print("3. Buscar contacto")
    print("4. Listar contactos")
    print("5. Salir")

def main():
    inicializar_archivo()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            agregar_contacto()
        elif opcion == '2':
            eliminar_contacto()
        elif opcion == '3':
            buscar_contacto()
        elif opcion == '4':
            listar_contactos()
        elif opcion == '5':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

main()
