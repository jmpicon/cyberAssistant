import psycopg2

def collect_user_data():
    # Conectarse a la base de datos PostgreSQL y recopilar datos
    # Ejemplo ficticio:
    user_data = {"actividad": "normal", "riesgos": ["bajo"]}
    return user_data

def generate_recommendations(threat_level):
    # Genera recomendaciones basadas en el nivel de amenaza
    # Ejemplo ficticio:
    if threat_level > 0.7:
        return "Reforzar contraseñas"
    else:
        return "Mantener prácticas actuales"