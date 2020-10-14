from django.db import models

# Model, dass dafür zuständig ist was unter Protokoll gespeichert wird
class Protokoll(models.Model):
    Thema = models.CharField(max_length=300, )
    Experimente = models.CharField(max_length=300, )
    Theorie = models.CharField(max_length=300, )
#Model, dass dafür zuständig ist was unter Fachbereich gespeichert wird,
#es wird aber iwie nichts unter Fachbereich abgespeichert keine Ahnung warum
class ProtokollFach(models.Model):
    Fachbereich = models.CharField(max_length=30,)
