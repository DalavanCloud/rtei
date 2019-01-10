# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-09 13:46
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import taggit.managers
import wagtail.core.fields
import wagtail.core.models
import wagtail.search.index


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0040_page_draft_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('title_en', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_fr', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_es', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_ar', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('slug_en', models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_fr', models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_es', models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_ar', models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('url_path_en', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('url_path_fr', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('url_path_es', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('url_path_ar', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('seo_title_en', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('seo_title_fr', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('seo_title_es', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('seo_title_ar', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('search_description_en', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('search_description_fr', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('search_description_es', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('search_description_ar', models.TextField(blank=True, null=True, verbose_name='search description')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('title_en', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_fr', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_es', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_ar', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('slug_en', models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_fr', models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_es', models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_ar', models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('url_path_en', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('url_path_fr', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('url_path_es', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('url_path_ar', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('seo_title_en', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('seo_title_fr', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('seo_title_es', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('seo_title_ar', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('search_description_en', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('search_description_fr', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('search_description_es', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('search_description_ar', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('intro', models.TextField(blank=True)),
                ('body', wagtail.core.fields.RichTextField(blank=True)),
                ('body_en', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('body_fr', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('body_es', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('body_ar', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('date', models.DateField(verbose_name='Post date')),
                ('feed_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='BlogPageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='rtei.BlogPage')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rtei_blogpagetag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ResourceIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('title_en', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_fr', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_es', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_ar', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('slug_en', models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_fr', models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_es', models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_ar', models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('url_path_en', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('url_path_fr', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('url_path_es', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('url_path_ar', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('seo_title_en', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('seo_title_fr', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('seo_title_es', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('seo_title_ar', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('search_description_en', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('search_description_fr', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('search_description_es', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('search_description_ar', models.TextField(blank=True, null=True, verbose_name='search description')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='RTEIAncillaryPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('title_en', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_fr', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_es', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_ar', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('slug_en', models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_fr', models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_es', models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_ar', models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('url_path_en', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('url_path_fr', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('url_path_es', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('url_path_ar', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('seo_title_en', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('seo_title_fr', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('seo_title_es', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('seo_title_ar', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('search_description_en', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('search_description_fr', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('search_description_es', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('search_description_ar', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('body', wagtail.core.fields.RichTextField(blank=True)),
                ('body_en', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('body_fr', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('body_es', wagtail.core.fields.RichTextField(blank=True, null=True)),
                ('body_ar', wagtail.core.fields.RichTextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='RteiDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('year', models.CharField(blank=True, help_text='e.g. 1999', max_length=4, validators=[django.core.validators.RegexValidator(code='nomatch', message='Must be 4 numbers', regex='^\\d{4}$')])),
                ('file', models.FileField(blank=True, help_text='Use this to upload a file and list it as a resource', upload_to='documents', verbose_name='file')),
                ('external_url', models.CharField(blank=True, help_text='Use this to add an external website as a listed resource', max_length=1000, validators=[django.core.validators.URLValidator(message='Must be a valid URL')], verbose_name='External Link')),
                ('country', models.CharField(blank=True, max_length=256)),
                ('is_resource', models.BooleanField(default=True, help_text='Determines whether document appears on the Resources page.')),
                ('description', wagtail.core.fields.RichTextField(blank=True)),
                ('collection', models.ForeignKey(default=wagtail.core.models.get_root_collection_id, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Collection', verbose_name='collection')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text=None, through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tags')),
                ('uploaded_by_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='uploaded by user')),
            ],
            options={
                'get_latest_by': 'created_at',
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
        migrations.CreateModel(
            name='RTEIPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('title_en', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_fr', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_es', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_ar', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('slug_en', models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_fr', models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_es', models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_ar', models.SlugField(allow_unicode=True, help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('url_path_en', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('url_path_fr', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('url_path_es', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('url_path_ar', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('seo_title_en', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('seo_title_fr', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('seo_title_es', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('seo_title_ar', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('search_description_en', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('search_description_fr', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('search_description_es', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('search_description_ar', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('body', wagtail.core.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='tags',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='rtei.BlogPageTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
