"""Nautobot Example DNS Manager Forms."""

from nautobot.extras.forms import NautobotModelForm
from nautobot.utilities.forms import SlugField

from .models import DnsZoneModel, ARecordModel, CNameRecordModel


class DnsZoneModelForm(NautobotModelForm):
    slug = SlugField()

    class Meta:
        model = DnsZoneModel
        fields = [
            "name",
            "slug",
            "mname",
            "rname",
            "ttl",
            "refresh",
            "retry",
            "expire",
        ]


class ARecordModelForm(NautobotModelForm):
    slug = SlugField()

    class Meta:
        model = ARecordModel
        fields = [
            "name",
            "slug",
            "zone",
            "address",
            "ttl",
        ]


class CNameRecordModelForm(NautobotModelForm):
    slug = SlugField()

    class Meta:
        model = CNameRecordModel
        fields = [
            "name",
            "slug",
            "zone",
            "value",
            "ttl",
        ]
