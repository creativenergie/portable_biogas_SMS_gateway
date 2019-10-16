from .base import *

INSTALLED_APPS += [
    "corsheaders"  # CORS management - @link https://github.com/adamchainz/django-cors-headers
]

MIDDLEWARE.insert(0, "corsheaders.middleware.CorsMiddleware")

CORS_ORIGIN_ALLOW_ALL = True

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {"format": "{levelname} {asctime} {module} {message}", "style": "{"},
        "simple": {"format": "{levelname} {message}", "style": "{"},
    },
    "handlers": {
        "logfile": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "simple",
            "filename": str(ROOT_DIR / ".." / "log" / "django-debug.log"),
        },
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "simple",
        },
        "app_logfile": {
            "level": "DEBUG",
            "class": "logging.handlers.RotatingFileHandler",
            "formatter": "verbose",
            "filename": str(ROOT_DIR / ".." / "log" / "app.log"),
        },
    },
    "loggers": {
        "django.db.backends": {
            "handlers": ["logfile"],
            "level": "DEBUG",
            "propagate": False,
        },
        "django": {"handlers": ["logfile"], "level": "DEBUG", "propagate": False},
        "app": {"handlers": ["app_logfile"], "level": "DEBUG", "propagate": False},
    },
}
