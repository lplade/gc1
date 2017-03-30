from rest_framework import serializers
from .models import Ebook, Creator


class EbookSerializer(serializers.ModelSerializer):
    """Maps Model to JSON"""

    # http://stackoverflow.com/questions/20633313/django-rest-framework-get-related-model-field-in-serializer
    creator = CreatorSerializer(source='creator', read_only=True)

    class Meta:
        model = Ebook
        fields = ('ebook_id', 'creator', 'title')  # TODO do anything with other fields?


class CreatorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Creator
        fields = ('creator_id', 'name', 'birth_year', 'death_year')  # TODO do something with aliases?

