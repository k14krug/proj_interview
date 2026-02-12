from __future__ import annotations

import os
from pathlib import Path

from app import create_app


def _load_env_file() -> None:
    """Load environment variables from a local .env file (dev convenience).

    In production, environment should be provided by systemd/container tooling.
    """

    env_path = Path(__file__).resolve().parent / ".env"
    if not env_path.exists():
        return

    try:
        from dotenv import load_dotenv  # type: ignore

        load_dotenv(env_path, override=False)
        return
    except Exception:
        pass

    # Minimal fallback parser when python-dotenv isn't installed.
    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        os.environ.setdefault(key, value)


_load_env_file()

env_name = os.getenv("K2_ENV", "development")
app = create_app(env_name)


if __name__ == "__main__":
    port = int(os.getenv("K2_WEB_PORT", "5000"))
    debug = env_name.lower() == "development"
    app.run(port=port, debug=debug)

