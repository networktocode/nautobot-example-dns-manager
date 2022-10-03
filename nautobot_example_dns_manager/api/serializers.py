from rest_framework import serializers

from nautobot.extras.api.serializers import NautobotModelSerializer
from nautobot.ipam.api.nested_serializers import NestedIPAddressSerializer

from ..models import DnsZoneModel, ARecordModel, CNameRecordModel
from .nested_serializers import NestedDnsZoneModelSerializer


class DnsZoneModelSerializer(NautobotModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:nautobot_example_dns_manager-api:dnszonemodel-detail"
    )

    class Meta:
        model = DnsZoneModel
        fields = "__all__"


class ARecordModelSerializer(NautobotModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:nautobot_example_dns_manager-api:arecordmodel-detail"
    )
    zone = NestedDnsZoneModelSerializer()
    address = NestedIPAddressSerializer()

    class Meta:
        model = ARecordModel
        fields = "__all__"


class CNameRecordModelSerializer(NautobotModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:nautobot_example_dns_manager-api:cnamerecordmodel-detail"
    )
    zone = NestedDnsZoneModelSerializer()

    class Meta:
        model = CNameRecordModel
        fields = "__all__"
