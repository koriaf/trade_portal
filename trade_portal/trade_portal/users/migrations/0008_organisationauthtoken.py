# Generated by Django 2.2.10 on 2020-09-09 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0007_auto_20200806_2337"),
    ]

    operations = [
        migrations.CreateModel(
            name="OrganisationAuthToken",
            fields=[
                (
                    "uuid",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "access_token",
                    models.CharField(max_length=40, unique=True, verbose_name="Key"),
                ),
                (
                    "readable_name",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="For example, 'PC37/office3' - or any other text useful for you",
                        max_length=1024,
                    ),
                ),
                (
                    "org",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="oauth2_tokens",
                        to="users.Organisation",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="api_tokens",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="User",
                    ),
                ),
            ],
            options={
                "ordering": ("-created_at",),
            },
        ),
    ]
