class User:

       def __init__(self, num_registro, user, password, age, avatar, inventario, dificultad): #Aqui es donde se almacena la informacion del usuarioo
              self.num_registro = num_registro
              self.user = user
              self.password = password
              self.age = age
              self.avatar = avatar
              self.inventario = inventario
              self.dificultad = dificultad

       def mostrar(self): #aqui se le muestra la infromacion al usuario si es llamado
              return(f"Usuario registrado: {self.num_registro}\nUsuario: {self.user}\nContraseña: {self.password}\nEdad: {self.age}\nAvatar: {self.avatar}\nInventario: {self.inventario}\nDificultad: {self.dificultad}")