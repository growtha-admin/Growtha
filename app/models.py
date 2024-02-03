import os, random
from django.db import models
from django.apps import apps
from django.utils import timezone
from django.utils.timezone import datetime
from cloudinary.models import CloudinaryField
from ckeditor_uploader.fields import RichTextUploadingField
from decouple import config



def random_digits():
    return ''.join(random.choice('123456789') for i in range(5))

def hash_generator(initials):
    return initials + ''.join(random.choice('23456789') for i in range(3))



class BlogPost(models.Model):

    url_hash = models.SlugField(
        max_length=5, 
        default=random_digits(),
        primary_key=True,
    )

    title = models.CharField(
        max_length=1000, 
        blank=False, 
        default='', 
        help_text='Title of the Blog Article'
    )

    description = models.TextField(
        max_length=1000, 
        blank=False, 
        default=''
    )

    author = models.ForeignKey(
        'app.Author', 
        on_delete=models.CASCADE, 
        blank=False, 
        null=True, 
        default=''
    )

    tag = models.ForeignKey(
        'app.Tag',
        default='',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )


    if config('ENVIRONMENT') == 'PROD':
        image = CloudinaryField('image')
    else:
        image = models.ImageField(
            upload_to='assets/blog_image', 
            blank=False,
            null=False,
            default='assets/article_placeholder.png'
        )

    image_alt = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        default='',
        help_text='Alternative Text for the Image'
    ) 

    content = RichTextUploadingField()

    published_at = models.DateTimeField(
        default=datetime.now, 
        editable=True, 
        null=False, 
        blank=False
    )


    class Meta:
        ordering = ('title', 'published_at', 'url_hash', 'author',)
        verbose_name = 'Blog Post Content'
        verbose_name_plural = 'Blog Post Contents'

    def __str__(self):
        return self.url_hash




class Author(models.Model):

    author_hash = models.CharField(
        max_length=4, 
        default=hash_generator('a'),
        primary_key=True
    )

    first_name = models.CharField(
        max_length=50, 
        blank=False, 
        null=False, 
        default=''
    )

    last_name = models.CharField(
        max_length=50, 
        blank=False, 
        null=False, 
        default=''
    )

    biography = models.TextField(
        max_length=1000, 
        default='', 
        blank=False, 
        null=False
    )

    if config('ENVIRONMENT') == 'PROD':
        display_picture = CloudinaryField('image')
    else:
        display_picture = models.ImageField(
            upload_to='assets/author_picture', 
            blank=False, 
            null=False, 
            default=''
        )

    display_picture_alt = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        default='',
    )

    display_picture_alt = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        default='',
    )
    
    author_facebook = models.URLField(
        blank=True, 
        null=True, 
        default='', 
        help_text='Link to Author\'s Facebook Profile'
    )
    
    author_instagram = models.URLField(
        blank=True, 
        null=True, 
        default='', 
        help_text='Link to Author\'s Instagram Profile'
    )
   
    author_twitter = models.URLField(
        blank=True, 
        null=True, 
        default='', 
        help_text='Link to Author\'s Twitter Profile'
    )

    author_linkedin = models.URLField(
        blank=True, 
        null=True, 
        default='', 
        help_text='Link to Author\'s LinkedIn Profile'
    )

    author_website = models.URLField(
        blank=True, 
        null=True, 
        default='', 
        help_text='Link to Author\'s Website'
    )

    joined_at = models.DateField(
        default=datetime.now().date(),
        editable=True, 
        null=False, 
        blank=False, 
        help_text='Date the Author became a Member of the Growtha Writer\'s Council'
    )


    class Meta:
        ordering = ('first_name', 'last_name', 'joined_at', 'author_hash')

    def __str__(self):
        return self.first_name + ' ' + self.last_name




class Tag(models.Model):

    tag_hash = models.CharField(
        max_length=4, 
        default=hash_generator('t'), 
        blank=False,
        primary_key=True
    )

    tag_name = models.CharField(
        max_length=100, 
        default='', 
        verbose_name='Tag Name', 
        blank=False
    )


    class Meta:
        ordering = ('tag_name', 'tag_hash',)

    def __str__(self):
        return self.tag_name
