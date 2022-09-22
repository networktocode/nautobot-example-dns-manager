from nautobot.core.api import OrderedDefaultRouter

from . import views

router = OrderedDefaultRouter()
router.register("dnszonemodel", views.DnsZoneModelViewSet)
router.register("arecordmodel", views.ARecordModelViewSet)
router.register("cnamerecordmodel", views.CNameRecordModelViewSet)

urlpatterns = router.urls
