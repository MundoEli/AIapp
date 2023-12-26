from django.db import models


class TextModel(models.Model):
    text = models.TextField()

    def __str__(self):
        return f"TextModel(pk={self.pk})"
