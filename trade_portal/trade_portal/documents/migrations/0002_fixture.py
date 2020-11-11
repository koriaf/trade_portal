# Generated by Django 2.0.13 on 2019-06-12 08:41

from django.db import migrations

# import django_countries.fields


def create_FTAs(apps, schema_editor):
    """
    We can't import the Post model directly as it may be a newer
    version than this migration expects. We use the historical version.
    """
    FTA = apps.get_model("documents", "FTA")
    FTA.objects.bulk_create(
        [
            FTA(country=["CN", "AU"], name="China-Australia Free Trade Agreement"),
            FTA(
                country=["JP", "AU"],
                name="Japan-Australia Economic Partnership Agreement",
            ),
            FTA(
                country=[
                    "BN",
                    "MM",
                    "KH",
                    "ID",
                    "LA",
                    "MY",
                    "NZ",
                    "PH",
                    "SG",
                    "VN",
                    "AU",
                ],
                name="AANZFTA First Protocol",
            ),
        ]
    )


class Migration(migrations.Migration):

    dependencies = [
        ("documents", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(create_FTAs, migrations.RunPython.noop),
    ]
