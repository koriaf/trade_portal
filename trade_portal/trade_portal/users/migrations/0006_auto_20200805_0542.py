# Generated by Django 2.2.10 on 2020-08-04 19:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_auto_20200804_1853"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="user",
            options={
                "ordering": ("date_joined",),
                "verbose_name": "user",
                "verbose_name_plural": "users",
            },
        ),
        migrations.CreateModel(
            name="OrgRoleRequest",
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
                ("created_at", models.DateTimeField(default=django.utils.timezone.now)),
                (
                    "role",
                    models.CharField(
                        choices=[("trader", "Trader"), ("chambers", "Chambers")],
                        max_length=16,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("requested", "Requested"),
                            ("evidence", "Evidence"),
                            ("approved", "Approved"),
                            ("rejected", "Rejected"),
                        ],
                        default="requested",
                        max_length=16,
                    ),
                ),
                ("evidence", models.FileField(blank=True, null=True, upload_to="")),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="orgrequests_created",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "handled_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="orgrequests_handled",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "org",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.Organisation",
                    ),
                ),
            ],
            options={
                "ordering": ("-created_at",),
            },
        ),
    ]
