# Simulador de entrenamiento Pokémon

Proyecto educativo en Python que aplica programación orientada a objetos.

## Requisitos
- Python 3.9 o posterior
- No necesita librerías externas

## Ejecutar
Desde la carpeta `pokemon_simulator`:

```bash
python main.py
```

## Funciones
- Capturar Pokémon con estadísticas iniciales.
- Entrenar con mejoras predeterminadas o personalizadas.
- Mostrar estadísticas y calcular poder total.
- Contar los objetos creados durante la sesión.
- Liberar Pokémon y simular combates.

## Nota sobre `__del__`
Python no garantiza el momento exacto en que se ejecuta el destructor en todos los entornos. En esta aplicación, al retirar el Pokémon de la lista y eliminar la referencia local, normalmente se imprime el mensaje inmediatamente en CPython.
