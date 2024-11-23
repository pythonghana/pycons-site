from django.apps import AppConfig

class PyconsSiteConfig(AppConfig):
    name = 'pycons_site'
    label = 'pycons_site'
    verbose_name = "PyCons Site"

    def ready(self):
        from django.conf import apps
        # Dynamically include all sub-apps here
        sub_apps = [
            'about',
            'cms',
            'coc',
            'conference_schedule',
            'contact',
            'event',
            'faq',
            'fin_aid',
            'health_safety_guideline',
            'home',
            'privacypolicy',
            'registration',
            'schedule',
            'speakers',
            'sponsors',
            'sponsor_us',
            'talks',
            'tickets',
        ]

        # Automatically include sub-apps in INSTALLED_APPS
        for app in sub_apps:
            apps.get_app_config('pycons_site').add_app_config(f'pycons_site.{app}')
