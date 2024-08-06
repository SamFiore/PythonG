class Robot:
    def __init__(self, modelo, tipo):
        self.modelo = modelo
        self.tipo = tipo
        #self.funcionando = False
    
    def funcionando(self):
        self.funcionando = True
        print ("El robot", self.modelo, self.tipo, "esta en fucionamiento.")

    def nofuncionando(self):
        self.funcionando = False
        print ("El robot", self.modelo, self.tipo, "esta en mantenimiento.")

limpiador = Robot("LMP180", "Limpiador")
camara = Robot("Protec90", "Vigilancia")

print (type (limpiador))
print (type (camara))

print (limpiador.modelo , limpiador.tipo)
print (camara.modelo , camara.tipo)

limpiador.funcionando()
limpiador.nofuncionando()

camara.funcionando()
camara.nofuncionando()