from backend.apps.core.models import TimestampedModel, AbstractPerson


class Child(AbstractPerson, TimestampedModel):

    class Meta:
        db_table = 'child'

    def __str__(self):
        return f'Child<snils={self.snils}>'
