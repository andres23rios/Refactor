


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class UserManagement:
    def __init__(self):
        self.users = []

    def register_user(self):
        username = input("Ingrese un nombre de usuario: ")
        password = input("Ingrese una contraseña: ")
        self.users.append(User(username, password))
        print("Usuario registrado con éxito!")
