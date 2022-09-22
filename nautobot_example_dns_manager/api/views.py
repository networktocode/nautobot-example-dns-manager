from nautobot.extras.api.views import NautobotModelViewSet

from nautobot_example_dns_manager.models import DnsZoneModel, ARecordModel
from . import serializers


class DnsZoneModelViewSet(NautobotModelViewSet):
    queryset = DnsZoneModel.objects.all()
    serializer_class = serializers.DnsZoneModelSerializer


class ARecordModelViewSet(NautobotModelViewSet):
    queryset = ARecordModel.objects.all()
    serializer_class = serializers.ARecordModelSerializer
