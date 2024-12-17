from .base import INSTALLED_APPS, BASE_DIR, TEMPLATES, DEBUG

INSTALLED_APPS += ["django_jinja"]

TEMPLATES.insert(
    0,
    {
        "BACKEND": "django_jinja.jinja2.Jinja2",
        "APP_DIRS": True,
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "OPTIONS": {
            "match_extension": ".jinja.html",
            "match_regex": None,
            "app_dirname": "templates",
            "undefined": None,
            "newstyle_gettext": True,
            "extensions": [
                "jinja2.ext.do",
                "jinja2.ext.loopcontrols",
                "jinja2.ext.i18n",
                "django_jinja.builtins.extensions.CsrfExtension",
                "django_jinja.builtins.extensions.CacheExtension",
                "django_jinja.builtins.extensions.DebugExtension",
                "django_jinja.builtins.extensions.TimezoneExtension",
                "django_jinja.builtins.extensions.UrlsExtension",
                "django_jinja.builtins.extensions.StaticFilesExtension",
                "django_jinja.builtins.extensions.DjangoFiltersExtension",
            ],
            "filters": {
                "json_script": "django.template.defaultfilters.json_script",
            },
            "autoescape": True,
            "auto_reload": True,
            "translation_engine": "django.utils.translation",
        },
    },
)
