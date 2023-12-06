from flask import Flask

def create_app():
    app = Flask(__name__, template_folder='templates', static_folder='static')

    with app.app_context():
        # Importación de rutas
        from .routes import init_routes

        # Inicialización de rutas
        init_routes(app)

        return app