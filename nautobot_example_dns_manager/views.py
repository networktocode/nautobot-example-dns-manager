"""Nautobot Example DNS Manager Views."""

from nautobot.core.views import mixins as view_mixins

from .models import DnsZoneModel, ARecordModel, PTRRecordModel, CNameRecordModel

class DnsZoneModelUIViewSet(view_mixins.ObjectListViewMixin,
    view_mixins.ObjectDetailViewMixin,
    view_mixins.ObjectEditViewMixin,
    view_mixins.ObjectDestroyViewMixin,
):
    queryset = DnsZoneModel.objects.all()


class ARecordModelUIViewSet(view_mixins.ObjectListViewMixin,
    view_mixins.ObjectDetailViewMixin,
    view_mixins.ObjectEditViewMixin,
    view_mixins.ObjectDestroyViewMixin,):
    queryset = ARecordModel.objects.all()


class PTRRecordModelUIViewSet(view_mixins.ObjectListViewMixin,
    view_mixins.ObjectDetailViewMixin,
    view_mixins.ObjectEditViewMixin,
    view_mixins.ObjectDestroyViewMixin,):
    queryset = PTRRecordModel.objects.all()


class CNameRecordModelUIViewSet(view_mixins.ObjectListViewMixin,
    view_mixins.ObjectDetailViewMixin,
    view_mixins.ObjectEditViewMixin,
    view_mixins.ObjectDestroyViewMixin,):
    queryset = CNameRecordModel.objects.all()