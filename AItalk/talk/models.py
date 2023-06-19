from django.db import models


class Dialogue(models.Model):
    role = models.CharField(max_length=64)
    context = models.CharField(max_length=1024)

    def __str__(self):
        return self.context
