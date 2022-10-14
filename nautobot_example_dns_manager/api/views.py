from nautobot.extras.api.views import NautobotModelViewSet

from nautobot_example_dns_manager.models import DnsZoneModel, ARecordModel, CNameRecordModel
from . import serializers


class DnsZoneModelViewSet(NautobotModelViewSet):
    queryset = DnsZoneModel.objects.all()
    serializer_class = serializers.DnsZoneModelSerializer


class ARecordModelViewSet(NautobotModelViewSet):
    queryset = ARecordModel.objects.all()
    serializer_class = serializers.ARecordModelSerializer


class CNameRecordModelViewSet(NautobotModelViewSet):
    queryset = CNameRecordModel.objects.all()
    serializer_class = serializers.CNameRecordModelSerializer
