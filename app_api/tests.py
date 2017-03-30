from django.test import TestCase
from .models import Ebook
from .models import Creator
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse


# https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1

class EbookModelTestCase(TestCase):

    def setUp(self):
        self.ebook_id = 999997
        self.book_name = "Fine Work of Literature"
        self.book = Ebook(title=self.book_name)

    def test_model_can_create_a_book(self):
        old_count = Ebook.objects.count()
        self.book.save()
        new_count = Ebook.objects.count()
        self.assertNotEqual(old_count, new_count)


class AuthorModelTestCase(TestCase):

    def setUp(self):
        self.creator_id = 999998
        self.name = 'Writersworth, Herbert'
        self.birth_year = 1920
        self.death_year = 1979
        self.author = Creator(
            creator_id=self.creator_id,
            name=self.name,
            birth_year=1920,
            death_year=1979
        )

    def test_model_can_create_an_author(self):
        old_count = Creator.objects.count()
        self.author.save()
        new_count = Creator.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):
    """Test suite for the api views"""

    def setUp(self):
        """Define the test client and other test variables"""
        self.client = APIClient()
        self.ebook_data = {
            'ebook_id': '999997',
            'creator': {
                'creator_id': '999998',
                'name': 'Writersworth, Herbert',
                'birth_year': '1920',
                'death_year': '1979'
            },
            'title': 'Fine Work of Literature'
        }
