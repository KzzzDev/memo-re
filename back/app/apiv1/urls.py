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
    path('brains/<int:userid>/<int:noteid>/share',
         views.NoteShareCreateDestroyAPIView.as_view()),
    path('brains/<int:userid>/<int:noteid>/',
         views.NoteRetrieveUpdateDestroyAPIView.as_view()),
    path('brains/<int:userid>', views.NoteListCreateAPIView.as_view()),
]
