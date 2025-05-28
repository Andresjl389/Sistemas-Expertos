from collections import defaultdict

# Simulación de sesiones por usuario
sesiones = defaultdict(lambda: {"puntuacion": defaultdict(int), "preguntados": set()})

def get_sesion(usuario_id):
    return sesiones[usuario_id]

def reset_sesion(usuario_id):
    sesiones[usuario_id] = {"puntuacion": defaultdict(int), "preguntados": set()}
