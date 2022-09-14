"""Nautobot Example DNS Manager URL definitions."""

from django.urls import path

from nautobot.core.views.routers import NautobotUIViewSetRouter
from . import views

router = NautobotUIViewSetRouter()
router.register("DnsZoneModel", views.DnsZoneModelUIViewSet)

urlpatterns = []

urlpatterns += router.urls