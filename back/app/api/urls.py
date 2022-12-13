from django.urls import include, path
# from . import views
from .views import *
app_name = 'api'

urlpatterns = [
    path('api/jp', JPTestAPI.as_view()),
    path('api/us', USTestAPI.as_view()),
    path('api/br', BRTestAPI.as_view()),
    path('', index, name='index'),
]
