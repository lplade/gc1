# from django.shortcuts import render
from rest_framework import generics
from .serializers import EbookSerializer, CreatorSerializer
from .models import Ebook, Creator


class CreateEbookView(generics.ListCreateAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

    def perform_create(self, serializer):
        """Save the post date when creating a new ebook"""
        serializer.save()


class CreateCreatorView(generics.ListCreateAPIView):
    queryset = Creator.objects.all()
    serializer_class = CreatorSerializer

    def perform_create(self, serializer):
        serializer.save()


class EbookDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ebook.objects.all()
    serializer_class = EbookSerializer

