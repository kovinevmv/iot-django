from django.conf.urls import url

from backend.apps.authentication.views import current_user_view, login_view, logout_view

app_name = 'authentication'
urlpatterns = [
    # Current user
    url(f'current-user', current_user_view),

    # Auth
    url(f'login', login_view),
    url(f'logout', logout_view),
]
