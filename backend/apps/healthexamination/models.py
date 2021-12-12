from django.db import models

from backend.apps.core.models import TimestampedModel


class HealthExamination(TimestampedModel):

    type = models.CharField(max_length=20, help_text='Название обследования')
    date = models.DateField(help_text='Дата обследования')
    weight = models.FloatField(help_text='Вес, кг')
    height = models.FloatField(help_text='Рост, см')
    chest_circumference = models.FloatField(help_text='Размер груди, см')
    head_circumference = models.FloatField(help_text='Размер головы, см')
    teeth = models.PositiveSmallIntegerField(help_text='Количество зубов')

    child = models.ForeignKey('child.Child', on_delete=models.CASCADE)

    class Meta:
        db_table = 'health_examination'

    def __str__(self):
        return f'HealthExamination<id={self.id}, type={self.type}>'
