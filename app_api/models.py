from django.db import models

# https://gist.github.com/andreasvc/b3b4189120d84dec8857
# 		id (int): Gutenberg identifier of text
# 		author (str): Last name, First name
# 		title (str): title of work
# 		subjects (list of str): list of descriptive subjects; a subject may be
# 			hierarchical, e.g:
# 			'England -- Social life and customs -- 19th century -- Fiction'
# 		LCC (list of str): a list of two letter Library of Congress
# 			Classifications, e.g., 'PS'
# 		language (list of str): list of two letter language codes.
# 		type (str): 'Text', 'Sound', ...
# 		formats (dict of str, str pairs): keys are MIME types, values are URLs.
# 		download count (int): the number of times this ebook has been
# 			downloaded from the Gutenberg site in the last 30 days.


class Ebook(models.Model):
    ebook_id = models.IntegerField(unique=True)
    creator_id = models.ForeignKey('Creator', on_delete=models.CASCADE)
    title = models.CharField(max_length=128, blank=False)
    # subjects use another table
    # language use another table?
    type = models.CharField(max_length=128)  # do we need any besides 'text'
    # formats use another table? or just pull text
    download_count = models.IntegerField


# Creator is the DublinCore catchall term for authors
class Creator(models.Model):
    creator_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=128)  # Last name, first name
    aliases = models.TextField  # TODO serialize multiple names in JSON?
    birth_year = models.IntegerField
    death_year = models.IntegerField
    # Name + birth + death can be used to uniquely ID an author
