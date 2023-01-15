from os import environ
from django.conf import settings
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.views.generic import TemplateView, RedirectView
from rest_framework import routers
from accounts.views import CustomUserViewSet

router = routers.DefaultRouter()
router.register("api/v1/auth/users", CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(environ['DJANGO_ADMIN_URL'], admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('api/v1/auth/', include('rest_framework.urls')),  # DRFのログイン機能を表示
    path('api/v1/', include('apiv1.urls')),
]

# メディアに入ってるファイルにアクセスできるようにする
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),

        path(
            'api/schema/',
            SpectacularAPIView.as_view(),
            name='schema'),
        path(
            'api/schema/swagger-ui/',
            SpectacularSwaggerView.as_view(
                url_name='schema'),
            name='swagger-ui'),
        path(
            'api/schema/redoc/',
            SpectacularRedocView.as_view(
                url_name='schema'),
            name='redoc'),
    ]

# urlpatterns += re_path('', RedirectView.as_view(url='/')),
