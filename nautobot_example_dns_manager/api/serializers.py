from nautobot.extras.api.serializers import NautobotModelSerializer

from nautobot_example_dns_manager.models import DnsZoneModel, ARecordModel, CNameRecordModel


class DnsZoneModelSerializer(NautobotModelSerializer):
    class Meta:
        model = DnsZoneModel
        fields = "__all__"


class ARecordModelSerializer(NautobotModelSerializer):
    class Meta:
        model = ARecordModel
        fields = "__all__"


class CNameRecordModelSerializer(NautobotModelSerializer):
    class Meta:
        model = CNameRecordModel
        fields = "__all__"
