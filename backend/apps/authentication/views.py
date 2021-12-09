from django.contrib.auth import logout, authenticate, login
from django.core.exceptions import ValidationError
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
def login_view(request):
    data = request.data

    email = data.get('email', None)
    password = data.get('password', None)

    if email is None:
        raise ValidationError('Заполнение поля email обязательно для входа')

    if password is None:
        raise ValidationError('Заполнение поля пароль обязательно для входа')

    user = authenticate(request, email=email, password=password)

    if user is None:
        raise ValidationError(
            'Пользователь с данной почтой или паролем не найден')

    if not user.is_active:
        raise ValidationError('Пользователь был деактивирован')

    login(request, user)
    return {
        'email': user.email,
        'id': user.id
    }


@require_http_methods(["POST"])
def logout_view(request):
    logout(request)
    return {'ok': True}


@require_http_methods(["GET"])
def current_user_view(request):
    if request.user.is_authenticated:
        return request.user
    return {}
