from django.apps import AppConfig


class ApisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apis'

    def ready(self):
        print("figure this out")
        # import apis.signals  ####FIGURE OUT WHAT TO IMPORT HERE FROM ORIGINAL DJANGO REACT TUTORIAL


 
    