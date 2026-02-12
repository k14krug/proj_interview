from __future__ import annotations

import os

from flask import Flask

from .config import get_config
from .routes import register_routes


def create_app(env_name: str | None = None) -> Flask:
    env = (env_name or os.getenv("K2_ENV") or "development").lower()

    app = Flask(__name__)
    cfg = get_config(env)
    app.config.update(cfg.as_flask_dict())

    register_routes(app)
    return app
