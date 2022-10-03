from nautobot.extras.api.views import NautobotModelViewSet
from nautobot_example_dns_manager.models import DnsZoneModel, ARecordModel, CNameRecordModel

from .. import filters
from . import serializers


class DnsZoneModelViewSet(NautobotModelViewSet):
    queryset = DnsZoneModel.objects.all()
    serializer_class = serializers.DnsZoneModelSerializer
    filterset_class = filters.DnsZoneModelFilterSet


class ARecordModelViewSet(NautobotModelViewSet):
    queryset = ARecordModel.objects.prefetch_related("zone", "address")
    serializer_class = serializers.ARecordModelSerializer
    filterset_class = filters.ARecordModelFilterSet


class CNameRecordModelViewSet(NautobotModelViewSet):
    queryset = CNameRecordModel.objects.prefetch_related("zone")
    serializer_class = serializers.CNameRecordModelSerializer
    filterset_class = filters.CNameRecordModelFilterSet
