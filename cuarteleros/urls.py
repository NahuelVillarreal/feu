from django.urls import path
from cuarteleros import views


urlpatterns = [
    path('', views.standby, name="standby"),
]

