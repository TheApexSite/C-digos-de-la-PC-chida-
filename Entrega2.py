class Personaje:
    def __init__(self, nombre, elixir, daño, vida, rareza, tipo, habilidad):
        self.nombre = nombre
        self.elixir = elixir
        self.rareza = rareza
        self.tipo = tipo
        self.vida = vida
        self.daño = daño
        self.habilidad = habilidad
        
    def presentarse(self):
        return f"Soy {self.nombre}, un(a) {self.tipo} {self.rareza}, y mi habilidad especial es {self.habilidad}."

    def atacar(self):
        pass  #Las subclases van a cambiar esto para que hagan su ataque.


class AtaqueConPuerco:
    def realizar_ataque(self):
        return "Ataco montado en un puerco, causando daño rápido."


class AtaqueConCañon:
    def realizar_ataque(self):
        return "Disparo mi cañón a larga distancia, causando daño significativo."


class AtaqueConCargaElectrica:
    def realizar_ataque(self):
        return "Descargo electricidad, aturdiendo y causando gran daño."


# Definición de clases para los personajes
class Montapuercos(Personaje, AtaqueConPuerco):
    def atacar(self):
        return self.realizar_ataque()


class GiganteNoble(Personaje, AtaqueConCañon):
    def atacar(self):
        return self.realizar_ataque()


class MagoElectrico(Personaje, AtaqueConCargaElectrica):
    def atacar(self):
        return self.realizar_ataque()


# Creación de personajes
montapuercos = Montapuercos("Montapuercos", 4, 300, 1500, "Rara", "Tropa", "Velocidad de ataque montado en un puerco")
gigante_noble = GiganteNoble("Gigante Noble", 6, 600, 3700, "Común", "Tropa", "Ataca con cañón a larga distancia")
mago_electrico = MagoElectrico("Mago Eléctrico", 5, 200, 800, "Legendaria", "Tropa", "Descarga eléctrica que aturde")

# Lista
personajes = [montapuercos, gigante_noble, mago_electrico]

# Función para mostrar el menú de los personajea
def mostrar_personajes():
    print("\nPersonajes disponibles:")
    for i, personaje in enumerate(personajes, 1):
        print(f"{i}. {personaje.nombre} (Elixir: {personaje.elixir}, Vida: {personaje.vida}, Daño: {personaje.daño})")
    print(f"{len(personajes) + 1}. Salir")

# Función para el ataque de un personaje
def realizar_combate(personaje):
    print("\n--- COMIENZA EL COMBATE ---")
    print(personaje.presentarse())
    print(f"{personaje.nombre} ataca: {personaje.atacar()}")
    print("--- FIN DEL COMBATE ---\n")

# Bucle para elegir personajes y realizar ataques
def iniciar_juego():
    while True:
        mostrar_personajes()
        
        eleccion = input("Elige un personaje para realizar el ataque (número): ")
        
        if eleccion.isdigit():
            eleccion = int(eleccion)
            if 1 <= eleccion <= len(personajes):
                personaje_seleccionado = personajes[eleccion - 1]
                realizar_combate(personaje_seleccionado)
            elif eleccion == len(personajes) + 1:
                print("¡Gracias por jugar! ¡Hasta la próxima!")
                break
            else:
                print(f"Opción inválida. Por favor, elige un número entre 1 y {len(personajes) + 1}.")
        else:
            print("Por favor, introduce un número válido.")

        continuar = input("¿Quieres realizar otro combate? (1 para SÍ, cualquier otra tecla para NO): ")
        if continuar != "1":
            print("¡Gracias por jugar!")
            break

# Iniciar el juego
iniciar_juego()