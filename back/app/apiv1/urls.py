from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()

app_name = 'apiv1'
urlpatterns = [
    path('', include(router.urls)),
    path('friends/apply/<int:user_from>/',
         views.FriendRequestAnswerAPIView.as_view()),
    path('friends/apply/', views.FriendRequestApplyListAPIView.as_view()),
    path('friends/list/', views.FriendListAPIView.as_view()),
    path('friends/request/', views.FriendRequestListAPIView.as_view()),
    path('friends/<int:user_to>/', views.FriendDeleteAPIView.as_view()),
    path('friends/', views.FriendRequestAPIView.as_view()),
    path('brains/friends/<int:id>/', views.NoteListFriendAPIView.as_view()),
    path('brains/share/<int:note>/<int:user_to>/',
         views.NoteShareUpdateDestroyAPIView.as_view()),
    path('brains/share/request/answer/',
         views.NoteShareRequestAnswerListAPIView.as_view()),
    path('brains/share/request/',
         views.NoteShareRequestListAPIView.as_view()),
    path('brains/share/',
         views.NoteShareListCreateAPIView.as_view()),
    path('brains/<int:id>/',
         views.NoteRetrieveUpdateDestroyAPIView.as_view()),
    path('brains/', views.NoteListCreateAPIView.as_view()),
]
