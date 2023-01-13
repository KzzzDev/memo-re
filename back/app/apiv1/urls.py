from django.urls import path, include
from rest_framework import routers

from . import views
from .views import FriendListRequestAPIView
from .views import FriendRequestApplyAPIView
from .views import FriendRequestDeleteAPIView

router = routers.DefaultRouter()

app_name = 'apiv1'
urlpatterns = [
    path('', include(router.urls)),
    path('friends/request/', FriendListRequestAPIView.as_view()),
    path('friends/request/apply/<int:user_from>/',
         views.FriendRequestApplyAPIView.as_view()),
    path('friends/request/delete/<int:user_to>/',
         views.FriendRequestDeleteAPIView.as_view()),
    path('friends/<int:user_to>/', views.FriendDeleteAPIView.as_view()),
    path('friends/', views.FriendListRequestAPIView.as_view()),
    path('brains/<int:note>/share/',
         views.NoteShareCreateDestroyAPIView.as_view()),
    path('brains/<int:id>/',
         views.NoteRetrieveUpdateDestroyAPIView.as_view()),
    path('brains/', views.NoteListCreateAPIView.as_view()),
]
