from django.db import models


class Todo(models.Model):
    text = models.CharField(max_length=200)
    added_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'ToDos'

    def __str__(self):
        return self.text
