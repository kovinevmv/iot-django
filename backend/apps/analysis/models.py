from django.db import models

from backend.apps.core.models import TimestampedModel


class Analysis(TimestampedModel):

    date = models.DateField(help_text='Дата анализа')
    name = models.CharField(help_text='Название анализа', max_length=100)
    parametr = models.FloatField(help_text='Доза')
    reaction = models.CharField(max_length=255)

    child = models.ForeignKey('child.Child', on_delete=models.CASCADE)

    class Meta:
        db_table = 'analysis'

    def __str__(self):
        return f'Analysis<id={self.id}, name={self.name}>'
