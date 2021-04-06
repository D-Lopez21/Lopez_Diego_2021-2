from User import User

class Facil(User):
    def __init__(self, num_registro, user, password, age, avatar, inventario, dificultad, lives, clues):
        self.dificultad = dificultad
        self.lives = float(lives)
        self.clues = clues
        super().__init__(num_registro, user, password, age, avatar, inventario, "Facil")

    def mostrar(self):
        return(f"Usuario registrado: {self.num_registro}\nUsuario: {self.user}\nContraseña: {self.password}\nEdad: {self.age}\nAvatar: {self.avatar}\nInventario: {self.inventario}\nDificultad: {self.dificultad}\nVidas: {self.lives}\nPistas: {self.clues}")

class Normal(User):
    def __init__(self, num_registro, user, password, age, avatar, inventario, dificultad, lives, clues):
        self.dificultad = dificultad
        self.lives = float(lives)
        self.clues = clues
        super().__init__(num_registro, user, password, age, avatar, inventario, "Normal")

    def mostrar(self):
        return(f"Usuario registrado: {self.num_registro}\nUsuario: {self.user}\nContraseña: {self.password}\nEdad: {self.age}\nAvatar: {self.avatar}\nInventario: {self.inventario}\nDificultad: {self.dificultad}\nVidas: {self.lives}\nPistas: {self.clues}")

class Dificil(User):
    def __init__(self, num_registro, user, password, age, avatar, inventario, dificultad, lives, clues):
        self.dificultad = dificultad
        self.lives = float(lives)
        self.clues = clues
        super().__init__(num_registro, user, password, age, avatar, inventario, "Dificil")

    def mostrar(self):
        return(f"Usuario registrado: {self.num_registro}\nUsuario: {self.user}\nContraseña: {self.password}\nEdad: {self.age}\nAvatar: {self.avatar}\nInventario: {self.inventario}\nDificultad: {self.dificultad}\nVidas: {self.lives}\nPistas: {self.clues}")
