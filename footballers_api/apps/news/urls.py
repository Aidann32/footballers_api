from django.urls import path

from .views import CreateComment


urlpatterns = [
    path('comments/', CreateComment.as_view())
]
