from django.conf import settings


def test_django_settings_loaded():
    assert isinstance(settings.SECRET_KEY, str)
    assert settings.SECRET_KEY != ""
    assert isinstance(settings.ALLOWED_HOSTS, list)


def test_database_config():
    db = settings.DATABASES["default"]
    assert db["ENGINE"] == "django.db.backends.mysql"
    assert db["NAME"]
