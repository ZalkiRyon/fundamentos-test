import csv
import os

def solicitar_datos():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    correo = input("Ingrese su correo: ")
    telefono = input("Ingrese su teléfono: ")
    mensaje = input("Ingrese su mensaje: ")
    
    return [nombre, apellido, correo, telefono, mensaje]

def guardar_datos(datos):
    archivo = 'Datoseje1.csv'
    archivo_existe = os.path.isfile(archivo)

    with open(archivo, mode='a', newline='') as file:
        escritor = csv.writer(file)
        if not archivo_existe:
            escritor.writerow(["Nombre", "Apellido", "Correo", "Teléfono", "Mensaje"])
        escritor.writerow(datos)
    
    print("Mensaje enviado y guardado exitosamente.")

def main():
    datos = solicitar_datos()
    guardar_datos(datos)

main()
