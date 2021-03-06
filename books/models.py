import re
import json
import urllib

from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.db import models
from django.forms import ValidationError
from django.utils.html import format_html, mark_safe
from modelcluster.fields import ParentalKey
from wagtail.wagtailadmin.edit_handlers import (FieldPanel, InlinePanel,
                                                PageChooserPanel)
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import RichTextField, StreamField
from wagtail.wagtailcore.models import Orderable, Page
from wagtail.wagtaildocs.edit_handlers import DocumentChooserPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel

from allies.models import Ally
from openstax.functions import build_document_url, build_image_url
from snippets.models import FacultyResource, StudentResource, Subject


class Quotes(models.Model):
    quote_text = RichTextField()
    quote_author = models.CharField(max_length=255)
    quote_author_school = models.CharField(max_length=255)

    api_fields = ('quote_text', 'quote_author', 'quote_author_school', )

    panels = [
        FieldPanel('quote_text'),
        FieldPanel('quote_author'),
        FieldPanel('quote_author_school'),
    ]


class FacultyResources(models.Model):
    resource = models.ForeignKey(
        FacultyResource,
        null=True,
        help_text="Manage resources through snippets.",
        related_name='+'
    )

    def get_resource_description(self):
        return self.resource.description
    resource_description = property(get_resource_description)

    def get_resource_unlocked(self):
        return self.resource.unlocked_resource
    resource_unlocked = property(get_resource_unlocked)


    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+'
    )

    def get_resource_heading(self):
        return self.resource.heading
    resource_heading = property(get_resource_heading)

    def get_link_document(self):
        return build_document_url(self.link_document.url)
    link_document_url = property(get_link_document)

    def get_document_title(self):
        return self.link_document.title
    link_document_title = property(get_document_title)

    link_text = models.CharField(
        max_length=255, help_text="Call to Action Text")

    api_fields = ('resource_heading', 'resource_description', 'resource_unlocked',
                  'link_external', 'link_page',
                  'link_document_url', 'link_document_title', 'link_text', )

    panels = [
        SnippetChooserPanel('resource'),
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
        FieldPanel('link_text'),
    ]


class StudentResources(models.Model):
    resource = models.ForeignKey(
        StudentResource,
        null=True,
        help_text="Manage resources through snippets.",
        related_name='+'
    )

    def get_resource_heading(self):
        return self.resource.heading
    resource_heading = property(get_resource_heading)

    def get_resource_description(self):
        return self.resource.description
    resource_description = property(get_resource_description)

    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )
    link_document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        related_name='+'
    )

    def get_link_document(self):
        return build_document_url(self.link_document.url)
    link_document_url = property(get_link_document)

    def get_document_title(self):
        return self.link_document.title
    link_document_title = property(get_document_title)

    link_text = models.CharField(
        max_length=255, help_text="Call to Action Text")

    api_fields = ('resource_heading', 'resource_description',
                  'link_external', 'link_page',
                  'link_document_url', 'link_document_title', 'link_text', )

    panels = [
        SnippetChooserPanel('resource'),
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
        DocumentChooserPanel('link_document'),
        FieldPanel('link_text'),
    ]


class Authors(models.Model):
    name = models.CharField(max_length=255)
    university = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    senior_author = models.BooleanField(default=False)
    display_at_top = models.BooleanField(default=False)
    book = ParentalKey(
        'books.Book', related_name='book_contributing_authors', null=True, blank=True)

    api_fields = (
        'name', 'university', 'country', 'senior_author', 'display_at_top', )

    panels = [
        FieldPanel('name'),
        FieldPanel('university'),
        FieldPanel('country'),
        FieldPanel('senior_author'),
        FieldPanel('display_at_top'),
    ]


class AuthorBlock(blocks.StructBlock):
        name = blocks.CharBlock(required=True)
        university = blocks.CharBlock(required=False)
        country = blocks.CharBlock(required=False)
        senior_author = blocks.BooleanBlock(required=False)
        display_at_top = blocks.BooleanBlock(required=False)

        class Meta:
            icon = 'user'


class BookAlly(models.Model):
    ally = models.ForeignKey(
        Ally,
        null=True,
        help_text="Manage allies through snippets.",
        on_delete=models.SET_NULL,
        related_name='allies_ally'
    )

    def get_ally_heading(self):
        return self.ally.heading
    ally_heading = property(get_ally_heading)

    def get_ally_short_description(self):
        return self.ally.short_description
    ally_short_description = property(get_ally_short_description)

    def get_ally_color_logo(self):
        return build_image_url(self.ally.logo_color)
    ally_color_logo = property(get_ally_color_logo)

    book_link_url = models.URLField(
        blank=True, help_text="Call to Action Link")
    book_link_text = models.CharField(
        max_length=255, help_text="Call to Action Text")

    api_fields = ('ally_heading', 'ally_short_description', 'ally_color_logo', 'book_link_url',
                  'book_link_text', )

    panels = [
        FieldPanel('ally'),
        FieldPanel('book_link_url'),
        FieldPanel('book_link_text'),
    ]


class BookQuotes(Orderable, Quotes):
    quote = ParentalKey('books.Book', related_name='book_quotes')


class BookFacultyResources(Orderable, FacultyResources):
    book_faculty_resource = ParentalKey(
        'books.Book', related_name='book_faculty_resources')


class BookStudentResources(Orderable, StudentResources):
    book_student_resource = ParentalKey(
        'books.Book', related_name='book_student_resources')


class BookAllies(Orderable, BookAlly):
    book_ally = ParentalKey('books.Book', related_name='book_allies')


class Book(Page):
    created = models.DateTimeField(auto_now_add=True)
    cnx_id = models.CharField(
        max_length=255, help_text="This is used to pull relevant information from CNX.",
        blank=True, null=True)
    salesforce_abbreviation = models.CharField(max_length=255, blank=True, null=True)
    salesforce_name = models.CharField(max_length=255, blank=True, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL,
                                null=True, related_name='+')

    def get_subject_name(self):
        return self.subject.name

    subject_name = property(get_subject_name)
    updated = models.DateTimeField(auto_now=True)
    is_ap = models.BooleanField(default=False)
    description = RichTextField(
        blank=True, help_text="Description shown on Book Detail page.")
    cover = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    def get_cover_url(self):
        return build_document_url(self.cover.url)

    cover_url = property(get_cover_url)
    publish_date = models.DateField(blank=True, null=True)
    authors = StreamField([
        ('author', AuthorBlock()),
    ], blank=True, null=True)
    print_isbn_10 = models.CharField(max_length=255, blank=True, null=True)
    print_isbn_13 = models.CharField(max_length=255, blank=True, null=True)
    digital_isbn_10 = models.CharField(max_length=255, blank=True, null=True)
    digital_isbn_13 = models.CharField(max_length=255, blank=True, null=True)
    ibook_isbn_10 = models.CharField(max_length=255, blank=True, null=True)
    ibook_isbn_13 = models.CharField(max_length=255, blank=True, null=True)
    ibook_volume_2_isbn_10 = models.CharField(max_length=255, blank=True, null=True)
    ibook_volume_2_isbn_13 = models.CharField(max_length=255, blank=True, null=True)
    license_text = models.TextField(
        blank=True, null=True, help_text="Text blurb that describes the license.")
    license_name = models.CharField(
        max_length=255, blank=True, null=True, editable=False)
    license_version = models.CharField(
        max_length=255, blank=True, null=True, editable=False)
    license_url = models.CharField(
        max_length=255, blank=True, null=True, editable=False)
    high_resolution_pdf = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    def get_high_res_pdf_url(self):
        if self.high_resolution_pdf:
            return build_document_url(self.high_resolution_pdf.url)
        else:
            return None

    high_resolution_pdf_url = property(get_high_res_pdf_url)
    low_resolution_pdf = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    def get_low_res_pdf_url(self):
        if self.low_resolution_pdf:
            return build_document_url(self.low_resolution_pdf.url)
        else:
            return None

    low_resolution_pdf_url = property(get_low_res_pdf_url)
    student_handbook = models.ForeignKey(
        'wagtaildocs.Document',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )

    def get_student_handbook_url(self):
        return build_document_url(self.student_handbook.url)

    student_handbook_url = property(get_student_handbook_url)
    community_resource_url = models.URLField(blank=True)
    community_resource_cta = models.CharField(max_length=255, blank=True, null=True)
    coming_soon = models.BooleanField(default=False)
    ibook_link = models.URLField(blank=True, help_text="Link to iBook")
    ibook_link_volume_2 = models.URLField(blank=True, help_text="Link to secondary iBook")
    webview_link = models.URLField(
        blank=True, help_text="Link to CNX Webview book")
    concept_coach_link = models.URLField(
        blank=True, help_text="Link to Concept Coach")
    bookshare_link = models.URLField(
        blank=True, help_text="Link to Bookshare resources")
    amazon_coming_soon = models.BooleanField(default=False)
    amazon_link = models.URLField(blank=True, help_text="Link to Amazon")
    amazon_price = models.DecimalField(
        default=0.00, max_digits=6, decimal_places=2)
    amazon_blurb = models.TextField(blank=True)
    bookstore_coming_soon = models.BooleanField(default=False)
    bookstore_link = models.URLField(blank=True, help_text="Link to Bookstore")
    bookstore_blurb = models.TextField(blank=True)
    comp_copy_available = models.BooleanField(default=True)
    errata_link = models.URLField(
        blank=True, help_text="Link to view openstaxcollege.org errata")
    errata_corrections_link = models.URLField(
        blank=True, help_text="Link errata corrections")
    table_of_contents = JSONField(editable=False, blank=True, null=True)
    tutor_marketing_book = models.BooleanField(default=False)

    content_panels = Page.content_panels + [
        FieldPanel('cnx_id'),
        FieldPanel('salesforce_abbreviation'),
        FieldPanel('salesforce_name'),
        FieldPanel('publish_date'),
        SnippetChooserPanel('subject'),
        FieldPanel('is_ap'),
        FieldPanel('description', classname="full"),
        DocumentChooserPanel('cover'),
        InlinePanel('book_quotes', label="Quotes"),
        InlinePanel('book_allies', label="Allies"),
        InlinePanel('book_student_resources', label="Student Resources"),
        InlinePanel('book_faculty_resources', label="Instructor Resources"),
        InlinePanel('book_contributing_authors', label="Contributing Authors"),
        #Hide until we are pulling authors from CNX
        #StreamFieldPanel('authors'),
        FieldPanel('print_isbn_10'),
        FieldPanel('print_isbn_13'),
        FieldPanel('digital_isbn_10'),
        FieldPanel('digital_isbn_13'),
        FieldPanel('ibook_isbn_10'),
        FieldPanel('ibook_isbn_13'),
        FieldPanel('ibook_volume_2_isbn_10'),
        FieldPanel('ibook_volume_2_isbn_13'),
        FieldPanel('license_text'),
        DocumentChooserPanel('high_resolution_pdf'),
        DocumentChooserPanel('low_resolution_pdf'),
        DocumentChooserPanel('student_handbook'),
        FieldPanel('community_resource_url'),
        FieldPanel('community_resource_cta'),
        FieldPanel('coming_soon'),
        FieldPanel('ibook_link'),
        FieldPanel('ibook_link_volume_2'),
        FieldPanel('concept_coach_link'),
        FieldPanel('bookshare_link'),
        FieldPanel('amazon_coming_soon'),
        FieldPanel('amazon_link'),
        FieldPanel('amazon_price'),
        FieldPanel('amazon_blurb'),
        FieldPanel('bookstore_coming_soon'),
        FieldPanel('bookstore_link'),
        FieldPanel('bookstore_blurb'),
        FieldPanel('comp_copy_available'),
        FieldPanel('errata_link'),
        FieldPanel('errata_corrections_link'),
        FieldPanel('tutor_marketing_book'),
    ]

    api_fields = ('created',
                  'updated',
                  'slug',
                  'title',
                  'cnx_id',
                  'salesforce_abbreviation',
                  'salesforce_name',
                  'subject_name',
                  'is_ap',
                  'description',
                  'cover_url',
                  'book_quotes',
                  'book_allies',
                  'book_student_resources',
                  'book_faculty_resources',
                  'book_contributing_authors',
                  'publish_date',
                  'authors',
                  'print_isbn_10',
                  'print_isbn_13',
                  'digital_isbn_10',
                  'digital_isbn_13',
                  'ibook_isbn_10',
                  'ibook_isbn_13',
                  'ibook_volume_2_isbn_10',
                  'ibook_volume_2_isbn_13',
                  'license_text',
                  'license_name',
                  'license_version',
                  'license_url',
                  'high_resolution_pdf_url',
                  'low_resolution_pdf_url',
                  'student_handbook_url',
                  'community_resource_url',
                  'community_resource_cta',
                  'coming_soon',
                  'ibook_link',
                  'ibook_link_volume_2',
                  'webview_link',
                  'concept_coach_link',
                  'bookshare_link',
                  'amazon_coming_soon',
                  'amazon_link',
                  'amazon_price',
                  'amazon_blurb',
                  'bookstore_coming_soon',
                  'bookstore_link',
                  'bookstore_blurb',
                  'comp_copy_available',
                  'errata_link',
                  'errata_corrections_link',
                  'table_of_contents',
                  'tutor_marketing_book', )

    parent_page_types = ['books.BookIndex']

    @property
    def book_title(self):
        return format_html(
            '{}',
            mark_safe(self.book.title),
        )

    def get_slug(self):
        return 'books/{}'.format(self.slug)

    def book_urls(self):
        book_urls = []
        for field in self.api_fields:
            try:
                url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', getattr(self, field))
                if url:
                    book_urls.append(url)
            except(TypeError, AttributeError):
                pass
        return book_urls

    def clean(self):
        errors = {}

        if self.cnx_id:
            try:
                url = '{}/contents/{}.json'.format(
                    settings.CNX_ARCHIVE_URL, self.cnx_id)
                response = urllib.request.urlopen(url).read()
                result = json.loads(response.decode('utf-8'))

                self.license_name = result['license']['name']
                self.license_version = result['license']['version']
                self.license_url = result['license']['url']

                self.table_of_contents = result['tree']

            except urllib.error.HTTPError as err:
                errors.setdefault('cnx_id', []).append(err)

        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs):
        # Temporary fix to migrate authors to the new orderable streamfields
        authors = []
        for author in self.book_contributing_authors.all():
            author_json = {'type': 'author',
                        'value': {
                            'name': author.name,
                            'university': author.university,
                            'country': author.country,
                            'senior_author': author.senior_author,
                            'display_at_top': author.display_at_top,
                        }}
            authors.append(author_json)
        if self.authors != json.dumps(authors):
            self.authors = json.dumps(authors)

        self.webview_link = 'https://cnx.org/contents/' + self.cnx_id

        return super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.book_title


class BookIndex(Page):
    page_description = models.TextField()
    dev_standards_heading = models.CharField(
        max_length=255, blank=True, null=True)
    dev_standard_1_heading = models.CharField(
        max_length=255, blank=True, null=True)
    dev_standard_1_description = RichTextField()
    dev_standard_2_heading = models.CharField(
        max_length=255, blank=True, null=True)
    dev_standard_2_description = RichTextField()
    dev_standard_3_heading = models.CharField(
        max_length=255, blank=True, null=True)
    dev_standard_3_description = RichTextField()
    subject_list_heading = models.CharField(
        max_length=255, blank=True, null=True)

    @property
    def books(self):
        books = Book.objects.all().order_by('path')
        book_data = []
        for book in books:
            try:
                book_data.append({
                    'id': book.id,
                    'slug': 'books/{}'.format(book.slug),
                    'title': book.title,
                    'subject': book.subject.name,
                    'is_ap': book.is_ap,
                    'coming_soon': book.coming_soon,
                    'cover_url': book.cover_url,
                    'high_resolution_pdf_url': book.high_resolution_pdf_url,
                    'low_resolution_pdf_url': book.low_resolution_pdf_url,
                    'ibook_link': book.ibook_link,
                    'ibook_link_volume_2': book.ibook_link_volume_2,
                    'webview_link': book.webview_link,
                    'concept_coach_link': book.concept_coach_link,
                    'bookshare_link': book.bookshare_link,
                    'amazon_coming_soon': book.amazon_coming_soon,
                    'amazon_link': book.amazon_link,
                    'amazon_price': book.amazon_price,
                    'amazon_blurb': book.amazon_blurb,
                    'bookstore_coming_soon': book.bookstore_coming_soon,
                    'bookstore_link': book.bookstore_link,
                    'bookstore_blurb': book.bookstore_blurb,
                    'comp_copy_available': book.comp_copy_available,
                    'salesforce_abbreviation': book.salesforce_abbreviation,
                    'salesforce_name': book.salesforce_name,
                    'urls': book.book_urls(),
                })
            except Exception as e:
                print("Error: {}".format(e))
        return book_data

    content_panels = Page.content_panels + [
        FieldPanel('page_description'),
        FieldPanel('dev_standards_heading'),
        FieldPanel('dev_standard_1_heading'),
        FieldPanel('dev_standard_1_description'),
        FieldPanel('dev_standard_2_heading'),
        FieldPanel('dev_standard_2_description'),
        FieldPanel('dev_standard_3_heading'),
        FieldPanel('dev_standard_3_description'),
        FieldPanel('subject_list_heading'),
    ]

    api_fields = (
        'title',
        'page_description',
        'dev_standards_heading',
        'dev_standard_1_heading',
        'dev_standard_1_description',
        'dev_standard_2_heading',
        'dev_standard_2_description',
        'dev_standard_3_heading',
        'dev_standard_3_description',
        'subject_list_heading',
        'books'
    )

    parent_page_types = ['pages.HomePage']
    subpage_types = ['books.Book']
