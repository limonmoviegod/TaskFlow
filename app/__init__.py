from flask import Flask, jsonify

__version__ = "0.1.0"


def create_app():
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify(status="ok", version=__version__)

    return app
