"""Nautobot Example DNS Manager Views."""

from nautobot.core.views import mixins as view_mixins

from .models import DnsZoneModel, ARecordModel, CNameRecordModel
from .tables import DnsZoneModelTable


class DnsZoneModelUIViewSet(
    view_mixins.ObjectListViewMixin,
    view_mixins.ObjectDetailViewMixin,
    view_mixins.ObjectEditViewMixin,
    view_mixins.ObjectDestroyViewMixin,
    view_mixins.ObjectBulkDestroyViewMixin,
):
    queryset = DnsZoneModel.objects.all()
    table_class = DnsZoneModelTable


class ARecordModelUIViewSet(
    view_mixins.ObjectListViewMixin,
    view_mixins.ObjectDetailViewMixin,
    view_mixins.ObjectEditViewMixin,
    view_mixins.ObjectDestroyViewMixin,
    view_mixins.ObjectBulkDestroyViewMixin,
):
    queryset = ARecordModel.objects.all()


class CNameRecordModelUIViewSet(
    view_mixins.ObjectListViewMixin,
    view_mixins.ObjectDetailViewMixin,
    view_mixins.ObjectEditViewMixin,
    view_mixins.ObjectDestroyViewMixin,
    view_mixins.ObjectBulkDestroyViewMixin,
):
    queryset = CNameRecordModel.objects.all()
