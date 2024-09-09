class Carta:
    def __init__(self, nombre, vida, daño, alcance):
        self.nombre = nombre
        self.vida = vida
        self.daño = daño
        self.alcance = alcance
    
    def mostrar_atributos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Vida: {self.vida}")
        print(f"Daño: {self.daño}")
        print(f"Alcance: {self.alcance}")
        print()

    # Función para realizar el combate entre los dos personajes
    def atacar(self, otro_personaje):
        print(f"{self.nombre} ataca a {otro_personaje.nombre}")
        otro_personaje.vida -= self.daño
        print(f"{otro_personaje.nombre} tiene ahora {otro_personaje.vida} puntos de vida.\n")

# Atributos personajes
personaje1 = Carta("Mago Eléctrico", 800, 100, 5)
personaje2 = Carta("Gigante Noble", 3700, 600, 5)
personaje3 = Carta("Montapuercos", 1500, 300, 2)

# Función para simular la batalla
def pelea(personaje1, personaje2):
    print(f"Batalla entre: {personaje1.nombre} y {personaje2.nombre}\n")
    
    while personaje1.vida > 0 and personaje2.vida > 0:
        personaje1.atacar(personaje2)
        
        if personaje2.vida > 0:
            personaje2.atacar(personaje1)
    
    # Imprimir resultado pelea
    if personaje1.vida > 0:
        print(f"{personaje1.nombre} ganó la batalla!")
    else:
        print(f"{personaje2.nombre} ganó la batalla!")

# Mostramos atributos de los personajes
personaje2.mostrar_atributos()
personaje3.mostrar_atributos()

# Iniciar la pelea entre Gigante Noble y Montapuercos
pelea(personaje2, personaje3)
