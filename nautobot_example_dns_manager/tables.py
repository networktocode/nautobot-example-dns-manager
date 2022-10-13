"""Nautobot Example DNS Manager Tables."""

import django_tables2 as tables

from nautobot.utilities.tables import BaseTable, ToggleColumn

from .models import DnsZoneModel


class DnsZoneModelTable(BaseTable):
    class Meta(BaseTable.Meta):
        model = DnsZoneModel
