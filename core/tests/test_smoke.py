from django.apps import apps


def test_core_installed():
    assert apps.is_installed("core")
