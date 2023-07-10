import graphene
from graphene_django import DjangoObjectType

from product import models


class CategoryModelType(DjangoObjectType):
    class Meta:
        model = models.Category
        fields = ["title"]


class ProductModelType(DjangoObjectType):
    category = graphene.Field(CategoryModelType)

    class Meta:
        model = models.Product
        fields = ["title", "description", "category"]


class Query(graphene.ObjectType):
    all_products = graphene.List(ProductModelType)

    def resolve_all_products(self, info, **kwargs):
        return models.Product.objects.filter(is_deleted=False)

schema = graphene.Schema(query=Query) 