# Generated by Django 4.2.6 on 2023-11-23 19:41

from django.conf import settings
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="CustomUser",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        blank=True, max_length=254, verbose_name="email address"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("is_school_user", models.BooleanField(default=False)),
                ("is_government_user", models.BooleanField(default=False)),
                ("is_district_user", models.BooleanField(default=False)),
                ("is_approved", models.BooleanField(default=False)),
                ("state", models.CharField(blank=True, max_length=50, null=True)),
                ("District", models.CharField(blank=True, max_length=50, null=True)),
                ("state_id", models.CharField(blank=True, max_length=50, null=True)),
                ("s_category", models.CharField(blank=True, max_length=150, null=True)),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="DropoutPrediction",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("age", models.IntegerField()),
                ("gender", models.IntegerField()),
                ("caste", models.IntegerField()),
                ("distance", models.IntegerField()),
                ("income", models.IntegerField()),
                ("fee", models.IntegerField()),
                ("prediction", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Suggestion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("instructor_name", models.CharField(max_length=150)),
                ("district_name", models.CharField(max_length=150)),
                ("state_name", models.CharField(blank=True, max_length=150, null=True)),
                ("instruction", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="Suggestion_state_to_sch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("instructor_name", models.CharField(max_length=150)),
                ("school_name", models.CharField(max_length=150)),
                ("state_name", models.CharField(blank=True, max_length=150, null=True)),
                ("instruction", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="SuggestionDis",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("instructor_name", models.CharField(max_length=150)),
                ("school_name", models.CharField(max_length=150)),
                (
                    "district_name",
                    models.CharField(blank=True, max_length=150, null=True),
                ),
                ("state_name", models.CharField(blank=True, max_length=150, null=True)),
                ("instruction", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="SchoolYearData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.IntegerField()),
                ("total_students", models.IntegerField()),
                ("state", models.CharField(max_length=150)),
                ("district", models.CharField(max_length=150)),
                (
                    "school",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="contactEnquiry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150)),
                ("age", models.IntegerField()),
                ("gender", models.CharField(max_length=150)),
                ("caste", models.CharField(max_length=150)),
                ("s_category", models.CharField(max_length=150)),
                ("Distance", models.IntegerField()),
                ("area", models.CharField(max_length=150)),
                ("city", models.CharField(max_length=150)),
                ("income", models.IntegerField()),
                ("reason", models.CharField(max_length=150)),
                ("foccupation", models.CharField(max_length=150)),
                ("schoolindex", models.CharField(max_length=150)),
                ("mystate", models.CharField(max_length=150)),
                ("studentid", models.CharField(max_length=150)),
                ("Year", models.IntegerField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
