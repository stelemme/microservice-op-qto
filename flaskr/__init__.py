from flask import Flask

def create_app():
    # Create the app.
    app = Flask(__name__)

    # Add home blueprint to the app.
    from .blueprints import home
    app.register_blueprint(home.bp)

    # Add some-operation blueprint to the app.
    from .blueprints import qto
    app.register_blueprint(qto.bp)

    return app

