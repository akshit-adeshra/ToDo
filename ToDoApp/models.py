from django.db import models


class Todo(models.Model):
    text = models.CharField(max_length=200)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'ToDos'
        ordering = ['-updated_on']

    def __str__(self):
        return self.text
