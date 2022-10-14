"""Filter implementations."""
import django_filters
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
    ttl__gte = django_filters.NumberFilter(field_name="ttl", lookup_expr="gte")
    ttl__lte = django_filters.NumberFilter(field_name="ttl", lookup_expr="lte")

    class Meta:
        model = ARecordModel
        fields = "__all__"


class CNameRecordModelFilterSet(NautobotFilterSet):
    """Filter for filtering CNameRecordModel objects."""

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
    ttl__gte = django_filters.NumberFilter(field_name="ttl", lookup_expr="gte")
    ttl__lte = django_filters.NumberFilter(field_name="ttl", lookup_expr="lte")

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
    ttl__gte = django_filters.NumberFilter(field_name="ttl", lookup_expr="gte")
    ttl__lte = django_filters.NumberFilter(field_name="ttl", lookup_expr="lte")

    class Meta:
        model = DnsZoneModel
        fields = "__all__"
