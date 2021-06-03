import uuid

from django.db import models

class GeneralModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_of_creation = models.DateTimeField(auto_now_add=True, editable=False)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering =['date_of_creation']
        #abstract = True #no crea este modelo dentro de la base de datos, pues solo se usa para que los demás modelos hereden de esta