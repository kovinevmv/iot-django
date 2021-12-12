from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from backend.apps.child.models import Child
from backend.apps.core.models import TimestampedModel, UserAuth, AbstractPerson


class Parent(UserAuth, AbstractPerson, AbstractBaseUser, PermissionsMixin,
             TimestampedModel):

    phone_number = PhoneNumberField(null=True)
    send_messages = models.BooleanField(
        default=True, help_text='Присылать оповещения о новых событиях?')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    children = models.ManyToManyField(Child)

    class Meta:
        db_table = 'parent'

    def __str__(self):
        return f'Parent<id={self.id}, fullname={self.email}>'
