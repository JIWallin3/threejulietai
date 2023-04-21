from django.urls import path, include
from graphene_django.views import GraphQLView
from memory_graph.schema import schema

urlpatterns = [
    path("mem/graphql/", GraphQLView.as_view(graphiql=True, schema=schema)),
]