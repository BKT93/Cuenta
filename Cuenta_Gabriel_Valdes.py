class Cuenta:

    #Constructor
    def __init__(self,titular,cantidad=0):

        #Atributos de la clase
        self.titular = titular
        self.cantidad= cantidad

    def mostrar(self):
        print(f"El titular es {self.titular} y tiene la cantidad de {self.cantidad}")
    def ingresar(self,cantidad):
        if cantidad >= 0:
            print(f"La cantidad ingresada es {cantidad}")
    def retirar(self,cantidad):
        print(f"Se retira la suma de dinero de {cantidad}")
    
cuenta1 = Cuenta ("Gabriel", 5200)
cuenta1.mostrar()

cuenta1.ingresar(2000)
cuenta1.retirar(500)

#No se como realizar que el titular sea obligatorio y la cantidad opcional
#No hallo la forma de sumar la cantidad ingresada a la cantidad que ya hay en la cuenta



    



    






