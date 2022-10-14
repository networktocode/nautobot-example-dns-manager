"""Nautobot Example DNS Manager Organizational Models."""

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from nautobot.core.fields import AutoSlugField
from nautobot.core.models.generics import PrimaryModel


class DnsZoneModel(PrimaryModel):
    """Model representing DNS Zone and SOA record."""

    name = models.CharField(max_length=200, help_text="FQDN of the Zone, w/ TLD.")
    slug = AutoSlugField(populate_from="name")
    mname = models.CharField(max_length=200, help_text="FQDN of the Authoritative Name Server for Zone.")
    rname = models.EmailField(help_text="Admin Email for the Zone in the form user@zone.tld.")
    refresh = models.IntegerField(
        validators=[MinValueValidator(300), MaxValueValidator(2147483647)],
        default="86400",
        help_text="Number of seconds after which secondary name servers should query the master for the SOA record, to detect zone changes.",
    )
    retry = models.IntegerField(
        validators=[MinValueValidator(300), MaxValueValidator(2147483647)],
        default=7200,
        help_text="Number of seconds after which secondary name servers should retry to request the serial number from the master if the master does not respond.",
    )
    expire = models.IntegerField(
        validators=[MinValueValidator(300), MaxValueValidator(2147483647)],
        default=3600000,
        help_text="Number of seconds after which secondary name servers should stop answering request for this zone if the master does not respond. This value must be bigger than the sum of Refresh and Retry.",
    )
    ttl = models.IntegerField(
        validators=[MinValueValidator(300), MaxValueValidator(2147483647)], default=3600, help_text="Time To Live."
    )

    def get_absolute_url(self):
        return reverse("plugins:nautobot_example_dns_manager:dnszonemodel", args=[self.slug])

    def __str__(self):
        return self.name


class ARecordModel(PrimaryModel):
    """Model for representing A records."""

    zone = models.ForeignKey(DnsZoneModel, on_delete=models.PROTECT)
    slug = AutoSlugField(populate_from="name")
    name = models.CharField(
        max_length=200, help_text="Name of the Record. Will inherit the domain from the zone of which it is a part."
    )
    address = models.ForeignKey(to="ipam.IPAddress", on_delete=models.CASCADE, help_text="IP address for the record.")
    ttl = models.IntegerField(
        validators=[MinValueValidator(300), MaxValueValidator(2147483647)], default=14400, help_text="Time To Live."
    )

    def get_absolute_url(self):
        return reverse("plugins:nautobot_example_dns_manager:arecordmodel", args=[self.slug])

    def __str__(self):
        return self.name


class CNameRecordModel(PrimaryModel):
    """Model representing CName records."""

    zone = models.ForeignKey(DnsZoneModel, on_delete=models.PROTECT, help_text="Zone that the CName record belongs to.")
    name = models.CharField(help_text="DNS name of the CName record.", max_length=200)
    slug = AutoSlugField(populate_from="name")
    value = models.CharField(help_text="FQDN of where the CName record redirects to.", max_length=253)
    ttl = models.IntegerField(
        validators=[MinValueValidator(300), MaxValueValidator(2147483647)], default=14400, help_text="Time To Live."
    )

    def get_absolute_url(self):
        return reverse("plugins:nautobot_example_dns_manager:cnamerecordmodel", args=[self.slug])

    def __str__(self):
        return self.name
