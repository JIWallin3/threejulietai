from django.db import models
from uuid import uuid4


class Person(models.Model):
    class Gender(models.TextChoices):
        MALE = 1, 'Male'
        FEMALE = 3, 'Female'

    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    namespace = models.CharField(max_length=256, blank=True)
    name = models.CharField(max_length=256, blank=True)
    gender = models.PositiveSmallIntegerField(choices=Gender.choices, blank=True)
    # Personal, public or professional? What does a relationship table look like? exclude for now
    # TODO: Add relationship table and do something with this relationship field
    # relationship_type = models.ForeignKey("self", on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"


class Place(models.Model):
    pass


class RelationshipPersonPerson(models.Model):
    class RelationshipType(models.TextChoices):
        FAMILY = 1, 'Family'
        PERSONAL = 2, 'Personal'
        PROFESSIONAL = 3, 'Professional'
        PUBLIC = 4, 'Public'

    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    namespace = models.CharField(max_length=256)
    person1 = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name='person1')
    person2 = models.ForeignKey(Person, on_delete=models.DO_NOTHING, related_name='person2')
    relationship_type = models.PositiveSmallIntegerField(choices=RelationshipType.choices,
                                                         default=RelationshipType.PERSONAL)
    relationship_sentiment = models.FloatField(default=0.0)
    relationship_notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.person1} - {self.person2}'


class RelationshipPersonPlace(models.Model):
    class RelationshipType(models.TextChoices):
        FAMILY = 1, 'Family'
        PERSONAL = 2, 'Personal'
        PROFESSIONAL = 3, 'Professional'
        PUBLIC = 4, 'Public'

    uuid = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    namespace = models.CharField(max_length=256)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    relationship_type = models.PositiveSmallIntegerField(choices=RelationshipType.choices,
                                                         default=RelationshipType.PERSONAL)
    relationship_sentiment = models.FloatField(default=0.0)
    relationship_notes = models.TextField(blank=True)

    def __str__(self):
        return {self.relationship_notes}
