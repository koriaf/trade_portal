# Generated by Django 2.2.10 on 2020-06-17 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("documents", "0008_party_dot_separated_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="document",
            name="search_field",
            field=models.TextField(blank=True, default=""),
        ),
    ]
