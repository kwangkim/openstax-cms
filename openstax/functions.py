from django.conf import settings
from wagtail.wagtailcore.models import Site


def build_document_url(url):
    if url:
        site = Site.objects.get(is_default_site=True)
        if site.port == 80:
            folder = url.split('/')[1]
            filename = url.split('/')[-1]
            return "{}{}/{}".format(settings.MEDIA_URL, folder, filename)
        else:
            return "http://{}:{}{}".format(site.hostname, site.port, url)
    else:
        return None


def build_image_url(image):
    if image:
        site = Site.objects.get(is_default_site=True)
        if site.port == 80:
            return "{}{}".format(settings.MEDIA_URL, image.file)
        else:
            return "http://{}:{}/api/v0/images/{}".format(site.hostname, site.port, image.pk)
    else:
        return None
