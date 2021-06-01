from django.db import models

# Create your models here.

class PersonModel(models.Model):
    """Model definition for PersonModel."""
    name = models.CharField(max_length=50)
    age = models.SmallIntegerField()
    nit = models.SmallIntegerField()
    
    class Meta:
        """Meta definition for PersonModel."""

        verbose_name = 'PersonModel'
        verbose_name_plural = 'PersonModels'

    def __str__(self):
        return self.name
