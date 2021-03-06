from django.conf import settings
from django.db import models
from django.template.defaultfilters import slugify
import flickr_api
from flickr_api.method_call import call_api

# Enable caching
from django.core.cache import cache
flickr_api.enable_cache(cache)


class Portfolio(object):

    def __init__(self, user_id):
        """
        sections is a dictionary with keys as a title of the section and values as the flickr set ID for items to display in that section
        """
#        self.user = flickr_api.Person(id=user_id) # Not currently used
        self._sections = []

    def setSections(self, section_settings):
        for section in section_settings:
            self._sections.append(PortfolioSection(section['title'], section['photoset_id']))

    def getSections(self):
        return self._sections


class PortfolioSection(object):

    def __init__(self, title, photoset_id):
        self.title = title
        self.slug = slugify(title)
        self.photoset_id = photoset_id
        self.photoset = flickr_api.Photoset(id=photoset_id)

    def getPhotos(self):
        extras = ['url_sq', 'url_s', 'url_t', 'url_m', 'url_o', 'url_l', 'description']
        return self.photoset.getPhotos(extras=extras)



class TextSnippet(models.Model):
    internal_name = models.CharField(max_length=32)
    text = models.TextField(help_text="You can can format (bold, italic, lists, etc) your text like this: <a href=\"http://nestacms.com/docs/creating-content/markdown-cheat-sheet\">markdown</a>. If you want a line break without starting a whole new paragraph, end the line with two spaces.")

    def __unicode__(self):
        return self.internal_name


class Quote(models.Model):
    quote = models.TextField(help_text="You can can format (bold, italic, lists, etc) your text like this: <a href=\"http://nestacms.com/docs/creating-content/markdown-cheat-sheet\">markdown</a>. If you want a line break without starting a whole new paragraph, end the line with two spaces.")

    def __unicode__(self):
        return self.quote