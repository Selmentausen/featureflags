import os
from importlib import import_module

env_target = os.getenv("DJANGO_ENV", "local")
module = f"featureflags.settings.{env_target}"
globals().update(import_module(module).__dict__)
