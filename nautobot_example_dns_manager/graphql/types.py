import graphene_django_optimizer as gql_optimizer

from .. import models, filters


class DnsZoneModelType(gql_optimizer.OptimizedDjangoObjectType):
    """GraphQL Type for DnsZoneModel."""

    class Meta:
        model = models.DnsZoneModel
        filterset_class = filters.DnsZoneModelFilterSet


class ARecordModelType(gql_optimizer.OptimizedDjangoObjectType):
    """GraphQL Type for ARecordModel."""

    class Meta:
        model = models.ARecordModel
        filterset_class = filters.ARecordModelFilterSet


class CNameRecordModelType(gql_optimizer.OptimizedDjangoObjectType):
    """GraphQL Type for CNameRecordModel."""

    class Meta:
        model = models.CNameRecordModel
        filterset_class = filters.CNameRecordModelFilterSet


graphql_types = [DnsZoneModelType, ARecordModelType, CNameRecordModelType]
