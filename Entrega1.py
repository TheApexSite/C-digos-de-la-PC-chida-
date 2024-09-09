class Carta:
    def __init__(self, nombre, vida, daño):
        self.nombre = nombre
        self.vida = vida
        self.vida_inicial = vida  # Vida original para restaurarla
        self.daño = daño

    def mostrar_atributos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Vida: {self.vida}")
        print(f"Daño: {self.daño}")
        print()

    def atacar(self, otro_personaje):
        if self.vida > 0:
            print(f"{self.nombre} ataca a {otro_personaje.nombre}")
            otro_personaje.vida -= self.daño
            if otro_personaje.vida < 0:
                otro_personaje.vida = 0
            print(f"{otro_personaje.nombre} tiene ahora {otro_personaje.vida} puntos de vida.\n")

# Atributos de personajes
personajes = [
    Carta("Mago Eléctrico", 800, 100),
    Carta("Gigante Noble", 3700, 600),
    Carta("Montapuercos", 1500, 300)
]

# Función para mostrar la lista de personajes disponibles
def mostrar_personajes():
    print("\nPersonajes disponibles:")
    for i, personaje in enumerate(personajes, 1):
        print(f"{i}. {personaje.nombre} (Vida: {personaje.vida_inicial}, Daño: {personaje.daño})")

# Función para que el usuario elija un personaje
def elegir_personaje():
    while True:
        try:
            eleccion = int(input("Elige un personaje por su número: ")) - 1
            if 0 <= eleccion < len(personajes):
                return personajes[eleccion]
            else:
                print("Opción no válida. Inténtalo de nuevo.")
        except ValueError:
            print("Por favor, introduce un número válido.")

# Función para simular la batalla
def pelea(personaje1, personaje2):
    print(f"\nBatalla entre: {personaje1.nombre} y {personaje2.nombre}\n")

    # Volver la vida al valor inicial
    personaje1.vida = personaje1.vida_inicial
    personaje2.vida = personaje2.vida_inicial

    while personaje1.vida > 0 and personaje2.vida > 0:
        personaje1.atacar(personaje2)

        if personaje2.vida > 0:  # Solo atacar si el otro personaje sigue vivo
            personaje2.atacar(personaje1)

    # Imprimir resultado pelea
    if personaje1.vida > 0:
        print(f"{personaje1.nombre} ganó la batalla!")
    else:
        print(f"{personaje2.nombre} ganó la batalla!")

# Función para iniciar el proceso de pelea
def iniciar_pelea():
    while True:
        mostrar_personajes()

        print("\nElige el primer personaje:")
        personaje1 = elegir_personaje()

        print("\nElige el segundo personaje (no puede ser el mismo):")
        while True:
            personaje2 = elegir_personaje()
            if personaje2 != personaje1:
                break
            else:
                print("No puedes elegir el mismo personaje. Elige otro.")

        # Iniciar la pela
        pelea(personaje1, personaje2)

        # Preguntar al usuario si desea hacer otra pelea
        continuar = input("¿Te gustaría realizar otro combate? (s/n): ").lower()
        if continuar != 's':
            print("¡Gracias por jugar!")
            break

# Iniciar el combate
iniciar_pelea()