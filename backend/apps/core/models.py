import re

from django.contrib.auth.models import (BaseUserManager)
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


def get_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None


class TimestampedModelManager(models.Manager):
    def get_queryset(self):
        # Автоматическая фильтрация удаленных моделей через deletedAt
        return super(TimestampedModelManager,
                     self).get_queryset().filter(deletedAt__isnull=True)


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text='Дата/время создания объекта, автоматически заполняется')

    updated_at = models.DateTimeField(
        auto_now=True,
        help_text=
        'Дата/время обновления объекта, автоматически изменяется при изменении полей объекта'
    )

    deleted_at = models.DateTimeField(
        null=True,
        default=None,
        blank=True,
        help_text=
        'Дата/время удаления объекта, рекомендуется использовать данную метку для удаления, а не SQL DELETE команду'
    )

    objects = TimestampedModelManager()

    class Meta:
        abstract = True

        # Вывод значений в обратном хронологическом порядке для объектов
        ordering = ['-createdAt', '-updatedAt']


def is_digit_string(value):
    """ Проверка что строка - 11 цифр """
    if not value or isinstance(value, str):
        raise ValidationError('СНИЛС - это строка')
    if not re.search(r'^\d{11}$', value):
        raise ValidationError('СНИЛС содержит 11 цифр')


class Gender(models.TextChoices):
    """ Enum для пола """
    Male = 'М', _('М')
    Female = 'Ж', _('Ж')


class AbstractPerson(models.Model):
    """ Абстрактный класс для описания человека, подходит для родителя и ребенка """
    first_name = models.CharField(max_length=255, help_text='Имя человека')
    last_name = models.CharField(max_length=255, help_text='Фамилия человека')
    middle_name = models.CharField(max_length=255,
                                   help_text='Отчество человека',
                                   null=True)

    snils = models.CharField(max_length=11,
                             help_text='СНИЛС человека, 11 цифр',
                             null=False,
                             validators=[is_digit_string])

    gender = models.CharField(max_length=15,
                              help_text='Пол - М/Ж',
                              choices=Gender.choices)

    birth_date = models.DateField(help_text='Дата рождения', null=True)

    class Meta:
        abstract = True


class UserAuthManager(BaseUserManager):
    def create_user(self, **kwargs):
        email = kwargs.pop('email')
        password = kwargs.pop('password')

        if email is None:
            raise TypeError('Пользователь должен иметь почту')

        if password is None:
            raise TypeError('Пользователь должен иметь пароль')

        user = self.model(email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class UserAuth(models.Model):
    email = models.EmailField(db_index=True, unique=True, help_text='Почта')

    is_active = models.BooleanField(
        default=True,
        help_text='Активный пользователь, может ли авторизоваться')
    is_staff = models.BooleanField(default=False,
                                   help_text='Суперпользователь')

    objects = UserAuthManager()

    class Meta:
        abstract = True
        # db_table = 'user'

    def __str__(self):
        return f'User<email={self.email}>'
