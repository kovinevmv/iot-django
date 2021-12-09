# Generated by Django 3.2.6 on 2021-12-09 20:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('child', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HealthExamination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Дата/время создания объекта, автоматически заполняется')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Дата/время обновления объекта, автоматически изменяется при изменении полей объекта')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, help_text='Дата/время удаления объекта, рекомендуется использовать данную метку для удаления, а не SQL DELETE команду', null=True)),
                ('type', models.CharField(help_text='Название обследования', max_length=20)),
                ('date', models.DateField(help_text='Дата обследования')),
                ('weight', models.FloatField(help_text='Вес, кг')),
                ('height', models.FloatField(help_text='Рост, см')),
                ('chest_circumference', models.FloatField(help_text='Размер груди, см')),
                ('head_circumference', models.FloatField(help_text='Размер головы, см')),
                ('teeth', models.PositiveSmallIntegerField(help_text='Количество зубов')),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='child.child')),
            ],
            options={
                'db_table': 'health_examination',
            },
        ),
    ]
