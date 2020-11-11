# Generated by Django 2.2.10 on 2020-07-07 06:58

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ("documents", "0017_auto_20200707_1648"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="sending_jurisdiction",
            field=django_countries.fields.CountryField(default="AU", max_length=2),
        ),
    ]
