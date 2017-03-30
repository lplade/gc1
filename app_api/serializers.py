from rest_framework import serializers
from .models import Ebook, Creator


class CreatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Creator
        fields = ('creator_id', 'name', 'birth_year', 'death_year')  # TODO do something with aliases?


class EbookSerializer(serializers.ModelSerializer):
    """Maps Model to JSON"""

    # http://stackoverflow.com/questions/20633313/django-rest-framework-get-related-model-field-in-serializer
    creator = CreatorSerializer(read_only=True)

    class Meta:
        model = Ebook
        fields = ('ebook_id', 'creator', 'title')  # TODO do anything with other fields?

    # TODO make create() and update() methods

    # def create(self, validated_data):
    #     creator_data = validated_data.pop('creator')
    #     ebook = Ebook.objects.create(**validated_data)
    #     return ebook

    # def update(self, validated_data):
    #     creator_data = validated_data.pop('creator')




