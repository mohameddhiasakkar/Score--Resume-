from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import JsonResponse
from django.urls import include, path


def home(request):
    return JsonResponse({
        "status": "running",
        "message": "Score Resume API 🚀"
    })


urlpatterns = [
    path('', home),
    path('admin/', admin.site.urls),
    path('api/', include('core_api.urls')),
    path('api/', include('ai_engine.urls')),
]


if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )