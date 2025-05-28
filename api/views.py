# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from core.models import Environment, FeatureFlag, Organisation, Project

from .serializers import (
    EnvironmentSerializer,
    FeatureFlagSerializer,
    OrganisationSerializer,
    ProjectSerializer,
)


class OrgOwnedMixin:
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user) if hasattr(qs.model, "owner") else qs


class OrganisationViewSet(OrgOwnedMixin, viewsets.ModelViewSet):
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer
    permission_classes = [IsAuthenticated]


class ProjectViewSet(OrgOwnedMixin, viewsets.ModelViewSet):
    queryset = Project.objects.select_related("organization")
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]


class EnvironmentViewSet(OrgOwnedMixin, viewsets.ModelViewSet):
    queryset = Environment.objects.select_related("project__organisation")
    serializer_class = EnvironmentSerializer
    permission_classes = [IsAuthenticated]


class FeatureFlagViewSet(OrgOwnedMixin, viewsets.ModelViewSet):
    queryset = FeatureFlag.objects.select_related("environment__project__organisation")
    serializer_class = FeatureFlagSerializer
    permission_classes = [IsAuthenticated]
