from django.contrib.auth import logout, authenticate, login
from django.core.exceptions import ValidationError
from django.forms import model_to_dict
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods


@require_http_methods(["POST"])
def login_view(request):
    data = request.POST

    email = data.get('email', None)
    password = data.get('password', None)

    try:
        if email is None:
            raise Exception('Заполнение поля email обязательно для входа')

        if password is None:
            raise Exception('Заполнение поля пароль обязательно для входа')

        user = authenticate(request, email=email, password=password)

        if user is None:
            raise Exception(
                'Пользователь с данной почтой или паролем не найден')

        if not user.is_active:
            raise Exception('Пользователь был деактивирован')

        login(request, user)
        return JsonResponse({'email': user.email, 'id': user.id})

    except Exception as e:
        return JsonResponse({'error': str(e)})


@require_http_methods(["POST"])
def logout_view(request):
    logout(request)
    return JsonResponse({'ok': True})


@require_http_methods(["GET"])
def current_user_view(request):
    user = request.user if request.user.is_authenticated else None
    data = model_to_dict(user, fields=['email', 'last_name']) if user else user
    return JsonResponse({'user': data})
