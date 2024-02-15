import queue

# Crear la cola
cola_misiones = queue.Queue()

# Definir una lista de misiones con su dificultad
misiones = [
    {"nombre": "Misión 1", "dificultad": 3},
    {"nombre": "Misión 2", "dificultad": 2},
    {"nombre": "Misión 3", "dificultad": 5},
    {"nombre": "Misión 4", "dificultad": 1},
    {"nombre": "Misión 5", "dificultad": 4}
]

# Agregar las misiones a la cola
for mision in misiones:
    cola_misiones.put(mision)

# Mostrar las misiones en orden de dificultad
while not cola_misiones.empty():
    mision = cola_misiones.get()
    print(mision["nombre"])
