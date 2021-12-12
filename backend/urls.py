from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include

from backend.settings import SECURE_ADMIN_URL

urlpatterns = [
    # TODO add here urls like this
    url(
        'api/auth/',
        include('backend.apps.authentication.urls',
                namespace='authentication')),
]

static_url = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns.extend(static_url)

if SECURE_ADMIN_URL:
    urlpatterns.append(url(f'api/{SECURE_ADMIN_URL}/', admin.site.urls))
