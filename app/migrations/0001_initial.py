# Generated by Django 4.2 on 2024-02-21 13:05

import app.models
import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_hash', models.CharField(default=app.models.author_hash, max_length=4, primary_key=True, serialize=False)),
                ('first_name', models.CharField(default='', max_length=50)),
                ('last_name', models.CharField(default='', max_length=50)),
                ('biography', models.TextField(default='', max_length=1000)),
                ('display_picture', models.ImageField(default='', upload_to='assets/author_picture')),
                ('display_picture_alt', models.CharField(default='', max_length=100)),
                ('author_facebook', models.URLField(blank=True, default='', help_text="Link to Author's Facebook Profile", null=True)),
                ('author_instagram', models.URLField(blank=True, default='', help_text="Link to Author's Instagram Profile", null=True)),
                ('author_twitter', models.URLField(blank=True, default='', help_text="Link to Author's Twitter Profile", null=True)),
                ('author_linkedin', models.URLField(blank=True, default='', help_text="Link to Author's LinkedIn Profile", null=True)),
                ('author_website', models.URLField(blank=True, default='', help_text="Link to Author's Website", null=True)),
                ('joined_at', models.DateTimeField(default=datetime.datetime.now, help_text="Date the Author became a Member of the Growtha Writer's Council")),
            ],
            options={
                'ordering': ('first_name', 'last_name', 'joined_at', 'author_hash'),
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_hash', models.CharField(default=app.models.tag_hash, max_length=4, primary_key=True, serialize=False)),
                ('tag_name', models.CharField(default='', max_length=100, verbose_name='Tag Name')),
            ],
            options={
                'ordering': ('tag_name', 'tag_hash'),
            },
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('url_hash', models.SlugField(default=app.models.random_digits, max_length=5, primary_key=True, serialize=False)),
                ('title', models.CharField(default='', help_text='Title of the Blog Article', max_length=1000)),
                ('description', models.TextField(default='', max_length=1000)),
                ('image', models.ImageField(default='assets/article_placeholder.png', upload_to='assets/blog_image')),
                ('image_alt', models.CharField(default='', help_text='Alternative Text for the Image', max_length=100)),
                ('content', ckeditor_uploader.fields.RichTextUploadingField()),
                ('is_featured', models.BooleanField(default=False, help_text='Featured Content? (Will be displayed as Featured Content on the homepage)')),
                ('published_at', models.DateTimeField(default=datetime.datetime.now)),
                ('author', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='app.author')),
                ('tag', models.ManyToManyField(blank=True, to='app.tag')),
            ],
            options={
                'verbose_name': 'Blog Post Content',
                'verbose_name_plural': 'Blog Post Contents',
                'ordering': ('title', 'published_at', 'url_hash', 'author', 'is_featured'),
            },
        ),
    ]
