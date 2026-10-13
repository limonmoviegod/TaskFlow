from flask import Flask, jsonify

__version__ = "1.0.0"


def create_app():
    app = Flask(__name__)
    app.config["TASKS"] = []

    @app.get("/health")
    def health():
        return jsonify(status="ok", version=__version__)

    from .tasks import bp
    app.register_blueprint(bp)

    return app
