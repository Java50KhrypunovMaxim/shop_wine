from django.db import models

class Wine(models.Model):
    info = models.CharField(max_length=400, null=True)

    class Meta:
        verbose_name = "wine"

    def __str__(self):
        return f"Wine: {self.info} (id = {self.id})"

