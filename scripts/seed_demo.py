import os
import pathlib
import random
import sys

import django
from django.contrib.auth import get_user_model

from core.models import Environment, Evaluation, FeatureFlag, Organisation, Project

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "featureflags.settings")
django.setup()


def run():
    """Create one org, project, environments, a flag, and sample evaluations."""
    User = get_user_model()

    user, _ = User.objects.get_or_create(
        username="demo_owner", defaults={"email": "demo@example.com"}
    )
    user.set_password("demo1234")
    user.save()

    org, _ = Organisation.objects.get_or_create(name="Acme Inc.", owner=user)
    project, _ = Project.objects.get_or_create(name="Frontend", organisation=org)
    prod, _ = Environment.objects.get_or_create(name="prod", project=project)
    staging, _ = Environment.objects.get_or_create(name="staging", project=project)

    flag, _ = FeatureFlag.objects.get_or_create(
        key="new_checkout",
        environment=prod,
        defaults={"enabled": True, "percentage": 100},
    )

    for _ in range(200):
        Evaluation.objects.create(
            flag=flag,
            user_identifier=f"user_{random.randint(1, 50)}",
            result=random.choice([True, False]),
        )

    print("✅  Demo data seeded!")


if __name__ == "__main__":
    run()
