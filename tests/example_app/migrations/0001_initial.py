# Generated by Django 1.9.4 on 2016-04-03 09:36

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models

import meta_mixin.models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=255, verbose_name="Title")),
                ("og_title", models.CharField(max_length=255, verbose_name="Opengraph title", blank=True)),
                ("twitter_title", models.CharField(max_length=255, verbose_name="Twitter title", blank=True)),
                ("schemaorg_title", models.CharField(max_length=255, verbose_name="Schema.org title", blank=True)),
                ("slug", models.SlugField(verbose_name="slug")),
                ("abstract", models.TextField(verbose_name="Abstract")),
                ("meta_description", models.TextField(blank=True, default="", verbose_name="Post meta description")),
                ("meta_keywords", models.TextField(blank=True, default="", verbose_name="Post meta keywords")),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_modified", models.DateTimeField(auto_now=True)),
                (
                    "date_published",
                    models.DateTimeField(default=django.utils.timezone.now, verbose_name="Published Since"),
                ),
                ("date_published_end", models.DateTimeField(blank=True, null=True, verbose_name="Published Until")),
                (
                    "main_image",
                    models.ImageField(blank=True, null=True, upload_to="images", verbose_name="Main image"),
                ),
                ("text", models.TextField(blank=True, default="", verbose_name="Post text")),
                ("image_url", models.CharField(blank=True, max_length=200, null=True)),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Author",
                    ),
                ),
            ],
            options={
                "verbose_name": "blog article",
                "get_latest_by": "date_published",
                "ordering": ("-date_published", "-date_created"),
                "verbose_name_plural": "blog articles",
            },
            bases=(meta_mixin.models.ModelMeta, models.Model),
        ),
    ]
