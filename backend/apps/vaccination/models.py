from django.db import models

from backend.apps.core.models import TimestampedModel


class Vaccination(TimestampedModel):

    date = models.DateField(help_text='Дата вакцинации')
    name = models.CharField(help_text='Название вакцины', max_length=100)
    series = models.CharField(help_text='Серия', max_length=20)
    quantity = models.FloatField(help_text='Доза')
    reaction = models.CharField(max_length=255)

    child = models.ForeignKey('child.Child', on_delete=models.CASCADE)

    class Meta:
        db_table = 'vaccination'

    def __str__(self):
        return f'Vaccination<id={self.id}, name={self.name}>'
