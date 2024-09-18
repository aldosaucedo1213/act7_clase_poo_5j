print("programacion poo")
# definicion de clases 
class perro:
    nombre="el trocitos"
    edad=4
    def morder(self):
        print("el perro me mordio")
    def datos_perro(self,nombre,edad ):
        print(f"nombre: {nombre} edad: {edad}")


# zona de creacion de objeto
pitbull=perro()

pitbull.datos_perro("el trocitos",4)
pitbull.morder()
