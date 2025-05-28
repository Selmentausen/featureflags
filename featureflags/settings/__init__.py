import os
from importlib import import_module

env_target = os.getenv("DJANGO_ENV", "local")
module = f"config.settings.{env_target}"
globals().update(import_module(module).__dict__)
