"""DNS Organizational Model"""

from tkinter.messagebox import RETRY
from django.db import models
from nautonot.core.models.generics import PrimaryModel
from django.urls import reverse
from nautobot.core.models

from nautobot.core.models.generics import OrganizationalModel
from nautobot.core.ipam import IPAddress

class DnsZoneModel(PrimaryModel):
    """Model to represent a DNS Zone and SOA record.

    """
    name = models.CharField()
    mname = models.CharField()
    rname = models.EmailField()
    serial = models.PositiveBigIntegerField(min=1, max=4294967295)
    refresh = models.IntegerField()
    retry = models.IntegerField()
    expire = models.IntegerField()
    ttl = models.PositiveIntegerField(min=300, max=2147483647, default=3600)


class ARecordModel(OrganizationalModel):
    name = models.CharField()
    address = models.ForeignKey(to=IPAddress)
    ttl = models.PositiveIntegerField(min=300, max=2147483647, default=14400)


class PTRRecordModel(OrganizationalModel):
    address = models.ForeignKey(to=IPAddress)


class CNameRecordModel(OrganizationalModel):
    name = models.CharField()
    value = models.CharField()
    ttl = models.PositiveIntegerField(min=300, max=2147483647, default=14400)
