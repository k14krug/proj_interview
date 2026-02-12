from __future__ import annotations

import os
from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    env: str
    secret_key: str
    worker_enabled: bool

    def as_flask_dict(self) -> dict[str, object]:
        return {
            "ENV": self.env,
            "SECRET_KEY": self.secret_key,
        }


def _get_bool(name: str, default: bool = False) -> bool:
    raw = os.getenv(name)
    if raw is None:
        return default
    return raw.strip().lower() in {"1", "true", "yes", "y", "on"}


def get_config(env_name: str) -> AppConfig:
    env = env_name.lower()

    default_secret = "dev-change-me" if env == "development" else ""
    secret_key = os.getenv("K2_SECRET_KEY", default_secret)

    if env == "production" and not secret_key:
        raise RuntimeError("K2_SECRET_KEY must be set in production")

    worker_enabled = _get_bool("WORKER_ENABLED", default=False)

    return AppConfig(env=env, secret_key=secret_key, worker_enabled=worker_enabled)
