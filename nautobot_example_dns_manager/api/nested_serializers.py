from rest_framework import serializers

from nautobot.core.api import WritableNestedSerializer

from ..models import DnsZoneModel


class NestedDnsZoneModelSerializer(WritableNestedSerializer):

    url = serializers.HyperlinkedIdentityField(
        view_name="plugins-api:nautobot_example_dns_manager-api:dnszonemodel-detail"
    )

    class Meta:
        """Meta attributes."""

        model = DnsZoneModel
        fields = "__all__"
