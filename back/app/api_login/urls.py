from rest_framework import routers
from django.urls import include, path
from . import views

router = routers.DefaultRouter()
router.register('api_login', views.BookViewSet)

app_name = 'api_login'
urlpatterns = [
    path('', include(router.urls)),
]
