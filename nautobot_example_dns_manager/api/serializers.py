from nautobot.extras.api.serializers import NautobotModelSerializer

from nautobot_example_dns_manager.models import DnsZoneModel, ARecordModel


class DnsZoneModelSerializer(NautobotModelSerializer):
    class Meta:
        model = DnsZoneModel
        fields = "__all__"


class ARecordModelSerializer(NautobotModelSerializer):
    class Meta:
        model = ARecordModel
        fields = "__all__"
