from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    EnvironmentViewSet,
    FeatureFlagViewSet,
    OrganisationViewSet,
    ProjectViewSet,
)

router = DefaultRouter()
router.register("organisation", OrganisationViewSet)
router.register("project", ProjectViewSet)
router.register("environment", EnvironmentViewSet)
router.register("featureflag", FeatureFlagViewSet)

urlpatterns = [
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    path("docs/", SpectacularSwaggerView.as_view(url_name="schema")),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
]
