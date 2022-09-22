"""Nautobot Example DNS Manager Views."""

from nautobot.core.views import mixins as view_mixins

from .models import DnsZoneModel, ARecordModel, CNameRecordModel
from .tables import DnsZoneModelTable, ARecordModelTable, CNameRecordModelTable
from .forms import DnsZoneModelForm, ARecordModelForm
from .api import serializers


class DnsZoneModelUIViewSet(
    view_mixins.ObjectListViewMixin,
    view_mixins.ObjectDetailViewMixin,
    view_mixins.ObjectEditViewMixin,
    view_mixins.ObjectDestroyViewMixin,
    view_mixins.ObjectBulkDestroyViewMixin,
):
    queryset = DnsZoneModel.objects.all()
    table_class = DnsZoneModelTable
    form_class = DnsZoneModelForm
    serializer_class = serializers.DnsZoneModelSerializer


class ARecordModelUIViewSet(
    view_mixins.ObjectListViewMixin,
    view_mixins.ObjectDetailViewMixin,
    view_mixins.ObjectEditViewMixin,
    view_mixins.ObjectDestroyViewMixin,
    view_mixins.ObjectBulkDestroyViewMixin,
):
    queryset = ARecordModel.objects.all()
    table_class = ARecordModelTable
    form_class = ARecordModelForm
    serializer_class = serializers.ARecordModelSerializer


class CNameRecordModelUIViewSet(
    view_mixins.ObjectListViewMixin,
    view_mixins.ObjectDetailViewMixin,
    view_mixins.ObjectEditViewMixin,
    view_mixins.ObjectDestroyViewMixin,
    view_mixins.ObjectBulkDestroyViewMixin,
):
    queryset = CNameRecordModel.objects.all()
    table_class = CNameRecordModelTable
