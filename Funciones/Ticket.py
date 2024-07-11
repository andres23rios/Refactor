


# Lista para almacenar los usuarios y tickets
users = []
tickets = []


# Función para registrar un nuevo usuario
def register_user():
    username = input("Ingrese un nombre de usuario: ")
    password = input("Ingrese una contraseña: ")
    users.append({'username': username, 'password': password})
    print("Usuario registrado con éxito!")


# Función para iniciar sesión
def login():
    while True:
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        for user in users:
            if user['username'] == username and user['password'] == password:
                print(f"Inicio de sesión exitoso! Bienvenido, {username}.")
                return True
        print(
            "Nombre de usuario o contraseña incorrectos. Inténtelo de nuevo.")


# Función para crear un ticket
def create_ticket():
    ticket = input("Ingrese el contenido del ticket: ")
    tickets.append(ticket)
    print("Ticket creado con éxito!")


# Función para eliminar un ticket
def delete_ticket():
    if not tickets:
        print("No hay tickets para eliminar.")
        return

    for i, ticket in enumerate(tickets):
        print(f"{i+1}. {ticket}")

    ticket_number = int(
        input("Ingrese el número del ticket que desea eliminar: "))
    if 1 <= ticket_number <= len(tickets):
        deleted_ticket = tickets.pop(ticket_number - 1)
        print(f"Ticket '{deleted_ticket}' eliminado con éxito!")
    else:
        print("Número de ticket inválido.")


# Función para ver los tickets
def view_tickets():
    if not tickets:
        print("No hay tickets para mostrar.")
    else:
        for i, ticket in enumerate(tickets):
            print(f"{i+1}. {ticket}")


# Menú principal
def main_menu():
    while True:
        print("\nMenú Principal")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")

        choice = input("Seleccione una opción: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            if login():
                # Submenú para creación y eliminación de tickets
                while True:
                    print("\nSubmenú de Tickets")
                    print("1. Crear ticket")
                    print("2. Eliminar ticket")
                    print("3. Ver tickets")
                    print("4. Cerrar sesión")

                    sub_choice = input("\nEstos son tus Tickets: ")

                    if sub_choice == '1':
                        create_ticket()
                    elif sub_choice == '2':
                        delete_ticket()
                    elif sub_choice == '3':
                        view_tickets()
                    elif sub_choice == '4':
                        print("Cerrando sesión.")
                        break
                    else:
                        print("Opción inválida, por favor intente de nuevo.")
        elif choice == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida, por favor intente de nuevo.")


# Ejecutar el menú principal
main_menu()
