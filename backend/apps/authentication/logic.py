from django.contrib.auth import get_user_model
from django.contrib.auth.backends import BaseBackend


class AuthenticationLogic(BaseBackend):
    """
    Custom Email Backend to perform authentication via email
    """
    def authenticate(self, request, username=None, email=None, password=None):
        email = username if username and not email else email
        user_model = get_user_model()
        try:
            # Try to fetch the user by searching email field
            user = user_model.objects.get(email=email)
            if user.check_password(password):
                return user
        except user_model.DoesNotExist:
            return None  # return None if custom user model does not exist
        except Exception as e:
            print(e)
            return None  # return None in case of other exceptions

    def get_user(self, user_id):
        my_user_model = get_user_model()
        try:
            return my_user_model.objects.get(pk=user_id)
        except my_user_model.DoesNotExist:
            return None
