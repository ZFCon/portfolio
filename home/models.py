from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel

from wagtail.core import blocks
from wagtail.core.fields import RichTextField

class HomePageProjects(Orderable):
    """Between 1 and 5 images for the home page carousel."""

    page = ParentalKey("home.HomePage", related_name="project_image")
    project_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    name = models.CharField(max_length=30, default='Name')
    description = RichTextField(features=['bold', 'italic', 'link'], blank=True)

    panels = [
        ImageChooserPanel("project_image"),
        FieldPanel('name'),
        FieldPanel('description')
        ]

class HomePage(Page):
    # main details
    profile = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    name = models.CharField(max_length=30, default='Name')
    career = models.CharField(max_length=100, default='Programmer')

    # about section
    about = RichTextField(features=['bold', 'italic', 'link'], blank=True)
    cv = models.URLField(blank=True)
    
    # detail
    address = models.CharField(max_length=100, default='Egypt, Giza')
    phone = models.CharField(max_length=20, default='+201000000000')
    email = models.EmailField(max_length=255, default='zfcon@zfcon.com')

    # social media
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            ImageChooserPanel('profile'),
            FieldPanel('name'),
            FieldPanel('career')
        ], "Main details"),
        MultiFieldPanel([InlinePanel('project_image', max_num=9)], 'Add Project Screenshot'),
        MultiFieldPanel([
            FieldPanel('about', classname='lead'),
            FieldPanel('cv')
        ], 'About me'),
        MultiFieldPanel([
            FieldPanel('address'),
            FieldPanel('phone'),
            FieldPanel('email')
        ],'Detail'),
        MultiFieldPanel([
            FieldPanel('facebook'),
            FieldPanel('twitter'),
            FieldPanel('linkedin')
        ],'Social media'),
    ]
