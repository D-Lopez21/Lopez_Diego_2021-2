from User import User

class Avatar(User):
    def __init__(self, user, password, age, avatar):
        self.avatar = avatar
        super().__init__(user, password, age, "Scharifker")

    def __init__(self, user, password, age, avatar):
        self.avatar = avatar
        super().__init__(user, password, age, "Eugenio Mendoza")

    def __init__(self, user, password, age, avatar):
        self.avatar = avatar
        super().__init__(user, password, age, "Pelusa")

    def __init__(self, user, password, age, avatar):
        self.avatar = avatar
        super().__init__(user, password, age, "Gandhi")

    def __init__(self, user, password, age, avatar):
        self.avatar = avatar
        super().__init__(user, password, age, "Estudiante de sistemas promedio")