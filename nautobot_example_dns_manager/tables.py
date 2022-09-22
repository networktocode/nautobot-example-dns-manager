"""Nautobot Example DNS Manager Tables."""

import django_tables2 as tables

from nautobot.utilities.tables import BaseTable, ToggleColumn

from .models import DnsZoneModel, ARecordModel, CNameRecordModel


class DnsZoneModelTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn(verbose_name="Zone Name")
    mname = tables.Column(verbose_name="Zone Name Server")
    rname = tables.EmailColumn(verbose_name="Admin Email")
    refresh = tables.Column(verbose_name="Refresh Time (s)")
    retry = tables.Column(verbose_name="Retry Time (s)")
    expire = tables.Column(verbose_name="Expire Time (s)")
    ttl = tables.Column(verbose_name="Time to Live (s)")

    class Meta(BaseTable.Meta):
        model = DnsZoneModel
        # fields determines the ordering of the columns
        fields = (
            "pk",
            "name",
            "mname",
            "rname",
            "ttl",
            "refresh",
            "retry",
            "expire",
        )
        # default_columns determines which columns are displayed
        default_columns = (
            "pk",
            "name",
            "mname",
            "rname",
            "refresh",
            "retry",
            "expire",
            "ttl",
        )


class ARecordModelTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn(verbose_name="Name")
    zone = tables.LinkColumn(verbose_name="DNS Zone")
    address = tables.LinkColumn(verbose_name="IP Address")
    ttl = tables.Column(verbose_name="Time To Live (s)")

    class Meta(BaseTable.Meta):
        model = ARecordModel
        # fields determines the ordering of the columns
        fields = ("pk", "name", "zone", "address", "ttl")
        # default_columns determines which columns are displayed
        default_columns = ("pk", "name", "zone", "address", "ttl")


class CNameRecordModelTable(BaseTable):
    pk = ToggleColumn()
    name = tables.LinkColumn(verbose_name="Name")
    zone = tables.LinkColumn(verbose_name="DNS Zone")
    value = tables.Column(verbose_name="Redirect")
    ttl = tables.Column(verbose_name="Time To Live (s)")

    class Meta(BaseTable.Meta):
        model = CNameRecordModel
        # fields determines the ordering of the columns
        fields = ("pk", "name", "zone", "value", "ttl")
        # default_columns determines which columns are displayed
        default_columns = ("pk", "name", "zone", "value", "ttl")
