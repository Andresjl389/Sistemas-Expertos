from expert_system.routes import (
    ruta_dificultad_respirar,
    ruta_fiebre,
    ruta_dolor_pecho,
    ruta_dolor_abdominal,
    ruta_mareo_debilidad,
    ruta_nausea_vomito,
    ruta_perdida_conciencia,
    ruta_brote_piel,
    ruta_accidente_golpe
    )

RUTAS = {
    "dificultad_respirar": ruta_dificultad_respirar,
    "fiebre": ruta_fiebre,
    "dolor_pecho": ruta_dolor_pecho,
    "dolor_abdominal": ruta_dolor_abdominal,
    "mareo_debilidad": ruta_mareo_debilidad,
    "nausea_vomito": ruta_nausea_vomito,
    "perdida_conciencia": ruta_perdida_conciencia,
    "brote_piel": ruta_brote_piel,
    "accidente_golpe": ruta_accidente_golpe
}

def evaluar_ruta(nombre_ruta: str, respuestas: dict) -> str:
    if nombre_ruta not in RUTAS:
        return "Ruta no válida."
    return RUTAS[nombre_ruta](respuestas)