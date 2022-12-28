from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
# router.register('notes', views.NoteViewSet)

app_name = 'apiv1'
urlpatterns = [
    path('', include(router.urls)),
    path('friends/request/', views.FriendCreateAPIView.as_view()),
    path('friends/request/', views.FriendUpdateAPIView.as_view()),
    path('friends/request/', views.FriendRequestDestroyAPIView.as_view()),
    path('friends/', views.FriendRetrieveAPIView.as_view()),
    path('friends/', views.FriendDestroyAPIView.as_view()),
    path('brains/<int:userid>/<int:noteid>/share',
         views.NoteShareCreateAPIView.as_view()),
    path('brains/<int:userid>/<int:noteid>/share',
         views.NoteShareDestroyAPIView.as_view()),
    path('brains/<int:userid>/<int:noteid>/',
         views.NoteRetrieveAPIView.as_view()),
    path('brains/<int:userid>/<int:noteid>/',
         views.NoteUpdateAPIView.as_view()),
    path('brains/<int:userid>/<int:noteid>/',
         views.NoteDestroyAPIView.as_view()),
    path('brains/<int:userid>', views.NoteListAPIView.as_view()),
    path('brains/<int:userid>', views.NoteCreateAPIView.as_view()),
]
