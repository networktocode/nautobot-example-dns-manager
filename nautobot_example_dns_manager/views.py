"""Nautobot Example DNS Manager Views."""

from nautobot.core.views import mixins as view_mixins

from .models import DnsZoneModel, ARecordModel, CNameRecordModel
from .tables import DnsZoneModelTable, ARecordModelTable, CNameRecordModelTable
from .forms import (
    ARecordModelFilterForm,
    CNameRecordModelFilterForm,
    DnsZoneModelFilterForm,
    DnsZoneModelForm,
    ARecordModelForm,
    CNameRecordModelForm,
)
from .filters import ARecordModelFilterSet, CNameRecordModelFilterSet, DnsZoneModelFilterSet
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
    filterset_class = DnsZoneModelFilterSet
    filterset_form_class = DnsZoneModelFilterForm
    action_buttons = ("add",)


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
    filterset_class = ARecordModelFilterSet
    filterset_form_class = ARecordModelFilterForm
    action_buttons = ("add",)


class CNameRecordModelUIViewSet(
    view_mixins.ObjectListViewMixin,
    view_mixins.ObjectDetailViewMixin,
    view_mixins.ObjectEditViewMixin,
    view_mixins.ObjectDestroyViewMixin,
    view_mixins.ObjectBulkDestroyViewMixin,
):
    queryset = CNameRecordModel.objects.all()
    table_class = CNameRecordModelTable
    form_class = CNameRecordModelForm
    serializer_class = serializers.CNameRecordModelSerializer
    filterset_class = CNameRecordModelFilterSet
    filterset_form_class = CNameRecordModelFilterForm
    action_buttons = ("add",)
