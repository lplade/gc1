from django.test import TestCase
from .models import Ebook
from .models import Creator


# https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1

class EbookModelTestCase(TestCase):

    def setUp(self):
        self.book_name = "A fine work of literature"
        self.book = Ebook(title=self.book_name)

    def test_model_can_create_a_book(self):
        old_count = Ebook.objects.count()
        self.book.save()
        new_count = Ebook.objects.count()
        self.assertNotEqual(old_count, new_count)


class AuthorModelTestCase(TestCase):

    def setUp(self):
        self.author_name = "Herbert Writersworth"
        self.author = Creator(name=self.author_name)

    def test_model_can_create_an_author(self):
        old_count = Creator.objects.count()
        self.author.save()
        new_count = Creator.objects.count()
        self.assertNotEqual(old_count, new_count)