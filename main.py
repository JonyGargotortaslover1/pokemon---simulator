from clases.pokemon import Pokemon

# Variable global: la lista compartida por las funciones del menú.
equipo = []


def pedir_entero(mensaje, minimo=0):
    """Solicita un entero válido y evita que el programa se cierre por error."""
    while True:
        try:
            valor = int(input(mensaje))
            if valor < minimo:
                print(f"Introduce un número mayor o igual que {minimo}.")
                continue
            return valor
        except ValueError:
            print("Entrada no válida: escribe un número entero.")


def capturar_pokemon():
    # Las variables de esta función son locales.
    nombre = input("Nombre: ").strip()
    tipo = input("Tipo: ").strip()
    if not nombre or not tipo:
        print("El nombre y el tipo no pueden quedar vacíos.")
        return

    ataque = pedir_entero("Ataque inicial: ")
    defensa = pedir_entero("Defensa inicial: ")
    salud = pedir_entero("Salud inicial: ", minimo=1)
    nuevo = Pokemon(nombre, tipo, ataque, defensa, salud)
    equipo.append(nuevo)  # Se guarda una referencia al mismo objeto.
    print(f"✅ {nuevo.nombre} fue añadido al equipo.")


def elegir_pokemon(mensaje):
    if not equipo:
        print("Tu equipo está vacío.")
        return None
    listar_pokemon()
    indice = pedir_entero(mensaje, minimo=1)
    if indice > len(equipo):
        print("No existe ese número de Pokémon.")
        return None
    return equipo[indice - 1]


def listar_pokemon():
    if not equipo:
        print("Todavía no has capturado Pokémon.")
        return
    for indice, pokemon in enumerate(equipo, start=1):
        print(f"{indice}. {pokemon.nombre} ({pokemon.tipo}) - Nivel {pokemon.nivel}")


def entrenar_pokemon():
    pokemon = elegir_pokemon("Número del Pokémon que entrenará: ")
    if pokemon is None:
        return
    print("Mejoras opcionales en orden: ataque, defensa, salud.")
    print("Pulsa Enter en la primera mejora para usar los valores predeterminados.")
    entrada = input("Mejoras separadas por comas (ej. 3,2,8): ").strip()
    try:
        if entrada:
            mejoras = tuple(int(parte.strip()) for parte in entrada.split(","))
            pokemon.entrenar(*mejoras)
        else:
            pokemon.entrenar()
    except ValueError as error:
        print(f"No se pudo entrenar: {error}")


def combatir():
    atacante = elegir_pokemon("Número del Pokémon atacante: ")
    if atacante is None:
        return
    objetivo = elegir_pokemon("Número del objetivo: ")
    if objetivo is None:
        return
    atacante.atacar(objetivo)


def liberar_pokemon():
    pokemon = elegir_pokemon("Número del Pokémon que liberarás: ")
    if pokemon is None:
        return
    equipo.remove(pokemon)
    nombre = pokemon.nombre
    del pokemon
    print(f"🕊️ {nombre} salió del equipo.")
    # __del__ se ejecuta cuando ya no quedan referencias al objeto.


def mostrar_todos():
    if not equipo:
        print("Todavía no hay Pokémon que mostrar.")
        return
    for pokemon in equipo:
        pokemon.mostrar_info()


def main():
    while True:
        print("\n===== SIMULADOR DE ENTRENAMIENTO POKÉMON =====")
        print("1. Capturar Pokémon 🐉")
        print("2. Entrenar Pokémon 💪")
        print("3. Ver información de todos 📋")
        print("4. Contar Pokémon creados 🧮")
        print("5. Liberar Pokémon 🕊️")
        print("6. Combatir ⚔️")
        print("0. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            capturar_pokemon()
        elif opcion == "2":
            entrenar_pokemon()
        elif opcion == "3":
            mostrar_todos()
        elif opcion == "4":
            Pokemon.total_pokemons()
        elif opcion == "5":
            liberar_pokemon()
        elif opcion == "6":
            combatir()
        elif opcion == "0":
            print("¡Gracias por entrenar! ¡Hasta la próxima! ⚡")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
