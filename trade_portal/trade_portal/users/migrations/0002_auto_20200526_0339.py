# Generated by Django 2.2.10 on 2020-05-25 17:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Organisation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                (
                    "type",
                    models.CharField(
                        choices=[("e", "Exporter"), ("c", "Chambers")], max_length=1
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "business_id",
                    models.CharField(
                        blank=True, help_text="ABN for Australia", max_length=64
                    ),
                ),
            ],
            options={
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="OrgMembership",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("since", models.DateTimeField(auto_now_add=True)),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("a", "Admin (can add users)"),
                            ("u", "User (can use org but not add users)"),
                        ],
                        default="u",
                        max_length=1,
                    ),
                ),
                (
                    "org",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.Organisation",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="organisation",
            name="users",
            field=models.ManyToManyField(
                related_name="users",
                through="users.OrgMembership",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
