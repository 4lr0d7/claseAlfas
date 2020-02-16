#Clase "Aparato eléctronico": *Encendido *Marca --Clase Dron() *helice *batería *color *tanque *volar *cargarGas
# encender()    volar()     apagar()    cargarGas()     aterrizar()     mostrarGas()
class AparatoElectronico:
    def __init__(self, encendido, marca):
        self.encendido = encendido
        self.marca = marca
    
class Dron(AparatoElectronico):
    def __init__(self, helice, bateria, color, tanque):
        AparatoElectronico.__init__(self, True, "Sony")
        self.helice = helice
        self.bateria = bateria
        self.color = color
        self.tanque = tanque
    
    def encender(self):
        if self.tanque > 0 and self.bateria == True:
            print("El Dron está encendido")
        else:
            print("El Dron no puede encender por falta de energía o tanque vacío")

    def volar(self):
        if self.bateria == True and self.tanque > 0:
            print("El Dron está volando")
        else:
            print("El Dron no puede volar porque no tiene suficiente bateria o tanque de gas")
    
    def apagar(self):
        print("El Dron está apagado")

    def cargarGas(self):
        self.tanque = self.tanque + 5
        print("El tanque tiene: ",self.tanque,"L", " de gasolina")

    def aterrizar(self):
        print("El dron está aterrizando")

    def mostrarGas(self):
        print(self.tanque, "L de gasolina")

dron = Dron("VRM", True, "Rojo", 50)
print (dron.marca)
dron.encender()
dron.apagar()
dron.cargarGas()
dron.aterrizar()
dron.mostrarGas()