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
]
