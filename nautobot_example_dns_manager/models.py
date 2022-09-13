"""DNS Organizational Model"""

from django.db import models

from django.urls import reverse
from nautobot.core.fields import AutoSlugField
from nautobot.core.models.generics import PrimaryModel

class DnsZoneModel(PrimaryModel):
    """Model to represent a DNS Zone and SOA record.

    """
    name = models.CharField()
    slug = AutoSlugField(populate_from='name')
    mname = models.CharField()
    rname = models.EmailField()
    serial = models.PositiveBigIntegerField(min=1, max=4294967295)
    refresh = models.IntegerField()
    retry = models.IntegerField()
    expire = models.IntegerField()
    ttl = models.PositiveIntegerField(min=300, max=2147483647, default=3600)


class ARecordModel(PrimaryModel):
    """Model for representing A records. 
    
    """
    name = models.CharField()
    address = models.ForeignKey(to="ipam.IPAddress")
    ttl = models.PositiveIntegerField(min=300, max=2147483647, default=14400)


class PTRRecordModel(PrimaryModel):
    """Model for 

    Args:
        OrganizationalModel (_type_): _description_
    """
    address = models.ForeignKey(to="ipam.IPAddress", on_delete=models.CASCADE)


class CNameRecordModel(PrimaryModel):
    name = models.CharField()
    value = models.CharField()
    ttl = models.PositiveIntegerField(min=300, max=2147483647, default=14400)
