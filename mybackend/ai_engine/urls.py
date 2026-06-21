from django.urls import path
from .views import analyze_resume, list_domains

urlpatterns = [
    path('domains/', list_domains),
    path('analyze/<int:resume_id>/', analyze_resume),
]