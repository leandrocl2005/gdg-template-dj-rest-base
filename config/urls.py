from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = (
    [
        path("", include("spectacular.urls")),
        # path("api/drf/token/", obtain_auth_token, name="drf_obtain_token"),
        path("api/jwt/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
        path(
            "api/jwt/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
        ),
        path("admin/", admin.site.urls),
        path("api/user/", include("userauths.urls")),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
