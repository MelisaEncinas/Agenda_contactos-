contactos = []             # Lista para almacenar los contactos


def mostrar_menu():
    print("\n--- Menú Principal ---")
    print("1. Agregar un nuevo contacto")
    print("2. Ver todos los contactos")
    print("3. Buscar un contacto por nombre")
    print("4. Eliminar un contacto")
    print("5. Salir de la aplicación")

def agregar_contacto():
    nombre = input("Ingrese el nombre del contacto: ")
    telefono = input("Ingrese el número de teléfono: ")
    email = input("Ingrese el correo electrónico: ")
    
    contacto = {
        "nombre": nombre,
        "telefono": telefono,
        "email": email
    }
    
    contactos.append(contacto)
    print(f"\nContacto {nombre} agregado exitosamente.")

def ver_contactos():
    if len(contactos) == 0:
        print("\nNo hay contactos guardados.")
    else:
        print("\n--- Lista de Contactos ---")
        for idx, contacto in enumerate(contactos, start=1):
            print(f"{idx}. Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")

def buscar_contacto():
    nombre_buscar = input("Ingrese el nombre del contacto que desea buscar: ")
    
    for contacto in contactos:
        if contacto['nombre'].lower() == nombre_buscar.lower():
            print(f"\nContacto encontrado: Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")
            return
    print(f"\nNo se encontró ningún contacto con el nombre '{nombre_buscar}'.")

def eliminar_contacto():
    nombre_eliminar = input("Ingrese el nombre del contacto que desea eliminar: ")
    
    for contacto in contactos:
        if contacto['nombre'].lower() == nombre_eliminar.lower():
            contactos.remove(contacto)
            print(f"\nContacto '{nombre_eliminar}' eliminado exitosamente.")
            return
    print(f"\nNo se encontró ningún contacto con el nombre '{nombre_eliminar}'.")

def salir_aplicacion():
    print("Saliendo de la aplicación...")
    exit()

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-5): ")
        
        if opcion == '1':
            agregar_contacto()
        elif opcion == '2':
            ver_contactos()
        elif opcion == '3':
            buscar_contacto()
        elif opcion == '4':
            eliminar_contacto()
        elif opcion == '5':
            salir_aplicacion()
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()
