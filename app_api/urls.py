from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateEbookView, CreateCreatorView

urlpatterns = {
    url(r'^ebooks/$', CreateEbookView.as_view(), name="create_ebook"),
    url(r'^creators/$', CreateCreatorView.as_view(), name="create_creator"),
}

urlpatterns = format_suffix_patterns(urlpatterns)
