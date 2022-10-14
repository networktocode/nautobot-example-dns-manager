"""Nautobot Example DNS Manager Forms."""

from django import forms

from nautobot.extras.forms import NautobotFilterForm, NautobotModelForm
from nautobot.utilities.forms import DynamicModelMultipleChoiceField, SlugField

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


class DnsZoneModelFilterForm(NautobotFilterForm):
    """Filtering/search form for `DnsZoneModel` objects."""

    model = DnsZoneModel

    q = forms.CharField(required=False, label="Search")
    name = forms.CharField(required=False)
    mname = forms.CharField(required=False, label="Primary server")
    rname = forms.EmailField(required=False, label="Admin email")
    refresh = forms.IntegerField(required=False, min_value=300, max_value=2147483647, label="Refresh timer")
    retry = forms.IntegerField(required=False, min_value=300, max_value=2147483647, label="Retry timer")
    expire = forms.IntegerField(required=False, min_value=300, max_value=2147483647, label="Expiry timer")
    ttl = forms.IntegerField(required=False, min_value=300, max_value=2147483647, label="Time to Live")
    ttl__gte = forms.IntegerField(required=False, label="TTL Greater/equal than")
    ttl__lte = forms.IntegerField(required=False, label="TTL Less/equal than")


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


class ARecordModelFilterForm(NautobotFilterForm):
    """Filtering/search form for `ARecordModel` objects."""

    model = ARecordModel

    q = forms.CharField(required=False, label="Search")
    name = forms.CharField(required=False)
    zone = DynamicModelMultipleChoiceField(required=False, queryset=DnsZoneModel.objects.all(), to_field_name="slug")
    ttl = forms.IntegerField(required=False, min_value=300, max_value=2147483647, label="Time to Live")
    ttl__gte = forms.IntegerField(required=False, label="TTL Greater/equal than")
    ttl__lte = forms.IntegerField(required=False, label="TTL Less/equal than")


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


class CNameRecordModelFilterForm(NautobotFilterForm):
    """Filtering/search form for `CNameRecordModel` objects."""

    model = CNameRecordModel

    q = forms.CharField(required=False, label="Search")
    name = forms.CharField(required=False)
    zone = DynamicModelMultipleChoiceField(required=False, queryset=DnsZoneModel.objects.all(), to_field_name="slug")
    value = forms.CharField(required=False, label="Redirect FQDN")
    ttl = forms.IntegerField(required=False, min_value=300, max_value=2147483647, label="Time to Live")
    ttl__gte = forms.IntegerField(required=False, label="TTL Greater/equal than")
    ttl__lte = forms.IntegerField(required=False, label="TTL Less/equal than")
