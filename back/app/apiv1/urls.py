from django.urls import path, include
from rest_framework import routers

from . import views
from .views import FriendRequestAPIView

router = routers.DefaultRouter()

app_name = 'apiv1'
urlpatterns = [
    path('', include(router.urls)),
    path('friends/request/', FriendRequestAPIView.as_view()),
    path('friends/', views.FriendRetrieveAPIView.as_view()),
    path('brains/<int:user_from>/<int:note>/share',
         views.NoteShareCreateDestroyAPIView.as_view()),
    path('brains/<int:user>/<int:id>/',
         views.NoteRetrieveUpdateDestroyAPIView.as_view()),
    path('brains/<int:user>', views.NoteListCreateAPIView.as_view()),
]
