from nautobot.extras.filters import NautobotFilterSet
from nautobot.utilities.filters import NaturalKeyOrPKMultipleChoiceFilter, SearchFilter

from nautobot_example_dns_manager.models import ARecordModel, CNameRecordModel, DnsZoneModel


class ARecordModelFilterSet(NautobotFilterSet):
    """Filter for filtering ARecordModel objects."""

    q = SearchFilter(
        filter_predicates={
            "name": "icontains",
        },
    )
    zone = NaturalKeyOrPKMultipleChoiceFilter(
        queryset=DnsZoneModel.objects.all(),
        label="DNS Zone (slug or ID)",
    )

    class Meta:
        model = ARecordModel
        fields = "__all__"


class CNameRecordModelFilterSet(NautobotFilterSet):
    """Filter for filtering ARecordModel objects."""

    q = SearchFilter(
        filter_predicates={
            "name": "icontains",
            "value": "icontains",
        },
    )

    zone = NaturalKeyOrPKMultipleChoiceFilter(
        queryset=DnsZoneModel.objects.all(),
        label="DNS Zone (slug or ID)",
    )

    class Meta:
        model = CNameRecordModel
        fields = "__all__"


class DnsZoneModelFilterSet(NautobotFilterSet):
    """Filter for filtering DnsZoneModel objects."""

    q = SearchFilter(
        filter_predicates={
            "name": "icontains",
            "mname": "icontains",
            "rname": "icontains",
        },
    )

    class Meta:
        model = DnsZoneModel
        fields = "__all__"
