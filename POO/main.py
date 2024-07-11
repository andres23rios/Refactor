
# main.py
from user import UserManagement
from ticket import TicketSystem

def main_menu(system):
    while True:
        print("\nMenú Principal")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")

        choice = input("Seleccione una opción: ")

        if choice == '1':
            system.users_manager.register_user()
        elif choice == '2':
            if system.login():
                # Submenú para creación y eliminación de tickets
                while True:
                    print("\nSubmenú de Tickets")
                    print("1. Crear ticket")
                    print("2. Eliminar ticket")
                    print("3. Ver tickets")
                    print("4. Cerrar sesión")

                    sub_choice = input("Seleccione una opción: ")

                    if sub_choice == '1':
                        system.create_ticket()
                    elif sub_choice == '2':
                        system.delete_ticket()
                    elif sub_choice == '3':
                        system.view_tickets()
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

if __name__ == "__main__":
    user_manager = UserManagement()
    system = TicketSystem(user_manager)
    main_menu(system)
