"""Nautobot Example DNS Manager URL definitions."""

from nautobot.core.views.routers import NautobotUIViewSetRouter
from . import views

router = NautobotUIViewSetRouter()
router.register("dnszonemodel", views.DnsZoneModelUIViewSet)
router.register("arecordmodel", views.ARecordModelUIViewSet)
router.register("cnamerecordmodel", views.CNameRecordModelUIViewSet)

urlpatterns = []

urlpatterns += router.urls
