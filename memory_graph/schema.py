import graphene
from graphene_django import DjangoObjectType
from memory_graph.models import Person, RelationshipPersonPerson, RelationshipPersonPlace


class PersonType(DjangoObjectType):
    class Meta:
        model = Person
        fields = "__all__"


class RelationshipPersonPersonType(DjangoObjectType):
    class Meta:
        model = RelationshipPersonPerson
        fields = "__all__"


class RelationshipPersonPlaceType(DjangoObjectType):
    class Meta:
        model = RelationshipPersonPlace
        fields = "__all__"


class Query(graphene.ObjectType):
    person_all = graphene.List(PersonType)
    relationship_person_person_all = graphene.List(RelationshipPersonPersonType)
    relationship_person_places_all = graphene.List(RelationshipPersonPlaceType)

    def resolve_all_persons(self, info, **kwargs):
        return Person.objects.all()

    def resolve_all_relationship_person_persons(self, info, **kwargs):
        return RelationshipPersonPerson.objects.all()

    def resolve_all_relationship_person_places(self, info, **kwargs):
        return RelationshipPersonPlace.objects.all()


schema = graphene.Schema(query=Query)
