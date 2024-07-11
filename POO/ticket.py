# ticket.py

class TicketSystem:
    def __init__(self, user_manager):
        self.users_manager = user_manager
        self.tickets = []

    def login(self):
        while True:
            username = input("Ingrese su nombre de usuario: ")
            password = input("Ingrese su contraseña: ")
            for user in self.users_manager.users:
                if user.username == username and user.password == password:
                    print(f"Inicio de sesión exitoso! Bienvenido, {username}.")
                    return True
            print("Nombre de usuario o contraseña incorrectos. Inténtelo de nuevo.")

    def create_ticket(self):
        ticket = input("Ingrese el contenido del ticket: ")
        self.tickets.append(ticket)
        print("Ticket creado con éxito!")

    def delete_ticket(self):
        if not self.tickets:
            print("No hay tickets para eliminar.")
            return

        for i, ticket in enumerate(self.tickets):
            print(f"{i+1}. {ticket}")

        ticket_number = int(input("Ingrese el número del ticket que desea eliminar: "))
        if 1 <= ticket_number <= len(self.tickets):
            deleted_ticket = self.tickets.pop(ticket_number - 1)
            print(f"Ticket '{deleted_ticket}' eliminado con éxito!")
        else:
            print("Número de ticket inválido.")

    def view_tickets(self):
        if not self.tickets:
            print("No hay tickets para mostrar.")
        else:
            for i, ticket in enumerate(self.tickets):
                print(f"{i+1}. {ticket}")
