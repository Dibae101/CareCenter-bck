# Generated by Django 3.2.3 on 2021-05-26 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Resume",
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
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("phone", models.PositiveIntegerField()),
                ("email", models.EmailField(max_length=254)),
                ("address", models.CharField(max_length=100)),
                ("city", models.CharField(max_length=100)),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("AL", "Alabama"),
                            ("AK", "Alaska"),
                            ("AZ", "Arizona"),
                            ("AR", "Arkansas"),
                            ("CA", "California"),
                            ("CO", "Colorado"),
                            ("CT", "Connecticut"),
                            ("DC", "Washington DC"),
                            ("DE", "Deleware"),
                            ("FL", "Florida"),
                            ("GA", "Georgia"),
                            ("HI", "Hawaii"),
                            ("ID", "Idaho"),
                            ("IL", "Illinios"),
                            ("IN", "Indiana"),
                            ("IA", "Iowa"),
                            ("KS", "Kansas"),
                            ("KY", "Kentucky"),
                            ("LA", "Louisiana"),
                            ("ME", "Maine"),
                            ("MD", "Maryland"),
                            ("MA", "Massachusetts"),
                            ("MI", "Michigan"),
                            ("MN", "Minnesota"),
                            ("MS", "Mississippi"),
                            ("MO", "Missouri"),
                            ("MT", "Montana"),
                            ("NE", "Nebraska"),
                            ("NV", "Nevada"),
                            ("NH", "New Hampshire"),
                            ("NJ", "New Jersey"),
                            ("NM", "New Mexico"),
                            ("NY", "New York"),
                            ("NC", "North Carolina"),
                            ("ND", "North Dakota"),
                            ("OH", "Ohio"),
                            ("OK", "Oklahoma"),
                            ("OR", "Oregon"),
                            ("PA", "Pennsylvania"),
                            ("RI", "Rhode Island"),
                            ("SC", "South Carolina"),
                            ("SD", "South Dakota"),
                            ("TN", "Tennessee"),
                            ("TX", "Texas"),
                            ("UT", "Utah"),
                            ("VT", "Vermont"),
                            ("VA", "Virgina"),
                            ("WA", "Washington"),
                            ("WV", "West Virginia"),
                            ("WI", "Wisconsin"),
                            ("WY", "Wyoming"),
                        ],
                        max_length=50,
                    ),
                ),
                ("zip_code", models.PositiveIntegerField(blank=True)),
                (
                    "citizen",
                    models.CharField(
                        blank=True, choices=[("Y", "Yes"), ("N", "No")], max_length=50
                    ),
                ),
                ("state_healthcare", models.CharField(blank=True, max_length=100)),
                ("state_license_number", models.CharField(blank=True, max_length=100)),
                ("recent_employer", models.CharField(blank=True, max_length=100)),
                ("prior_employer_2", models.CharField(blank=True, max_length=100)),
                ("prior_employer_3", models.CharField(blank=True, max_length=100)),
                ("immediate_supervisor", models.CharField(blank=True, max_length=100)),
                (
                    "may_we_contact",
                    models.CharField(
                        blank=True, choices=[("Y", "Yes"), ("N", "No")], max_length=50
                    ),
                ),
                ("address_1", models.CharField(blank=True, max_length=100)),
                ("city_1", models.CharField(blank=True, max_length=100)),
                (
                    "state_1",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("AL", "Alabama"),
                            ("AK", "Alaska"),
                            ("AZ", "Arizona"),
                            ("AR", "Arkansas"),
                            ("CA", "California"),
                            ("CO", "Colorado"),
                            ("CT", "Connecticut"),
                            ("DC", "Washington DC"),
                            ("DE", "Deleware"),
                            ("FL", "Florida"),
                            ("GA", "Georgia"),
                            ("HI", "Hawaii"),
                            ("ID", "Idaho"),
                            ("IL", "Illinios"),
                            ("IN", "Indiana"),
                            ("IA", "Iowa"),
                            ("KS", "Kansas"),
                            ("KY", "Kentucky"),
                            ("LA", "Louisiana"),
                            ("ME", "Maine"),
                            ("MD", "Maryland"),
                            ("MA", "Massachusetts"),
                            ("MI", "Michigan"),
                            ("MN", "Minnesota"),
                            ("MS", "Mississippi"),
                            ("MO", "Missouri"),
                            ("MT", "Montana"),
                            ("NE", "Nebraska"),
                            ("NV", "Nevada"),
                            ("NH", "New Hampshire"),
                            ("NJ", "New Jersey"),
                            ("NM", "New Mexico"),
                            ("NY", "New York"),
                            ("NC", "North Carolina"),
                            ("ND", "North Dakota"),
                            ("OH", "Ohio"),
                            ("OK", "Oklahoma"),
                            ("OR", "Oregon"),
                            ("PA", "Pennsylvania"),
                            ("RI", "Rhode Island"),
                            ("SC", "South Carolina"),
                            ("SD", "South Dakota"),
                            ("TN", "Tennessee"),
                            ("TX", "Texas"),
                            ("UT", "Utah"),
                            ("VT", "Vermont"),
                            ("VA", "Virgina"),
                            ("WA", "Washington"),
                            ("WV", "West Virginia"),
                            ("WI", "Wisconsin"),
                            ("WY", "Wyoming"),
                        ],
                        max_length=50,
                    ),
                ),
                ("zip_code_1", models.PositiveIntegerField(blank=True)),
                ("position", models.CharField(blank=True, max_length=100)),
                (
                    "hours_available",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Sun-Sat", "Any Hours Sun-Sat"),
                            ("Mon-Fri", "Any Hours Mon-Fri"),
                            ("Mornings", "Mornings Only"),
                            ("Evenings", "Evenings Only"),
                            ("Night", "Night Shifts"),
                            ("Weekends", "Weekends Only"),
                            ("Other", "Others"),
                        ],
                        max_length=50,
                    ),
                ),
                ("specify_hours_detail", models.CharField(blank=True, max_length=300)),
                ("reference_1", models.CharField(blank=True, max_length=100)),
                ("reference_2", models.CharField(blank=True, max_length=100)),
                ("phone_1", models.PositiveIntegerField(blank=True)),
                ("work_at", models.CharField(blank=True, max_length=300)),
                ("learn_about", models.CharField(blank=True, max_length=100)),
                (
                    "engage_other",
                    models.CharField(
                        blank=True, choices=[("Y", "Yes"), ("N", "No")], max_length=50
                    ),
                ),
                (
                    "further_study",
                    models.CharField(
                        blank=True, choices=[("Y", "Yes"), ("N", "No")], max_length=50
                    ),
                ),
                (
                    "emergency_contact_name",
                    models.CharField(blank=True, max_length=100),
                ),
                ("emergency_contact_phone", models.PositiveIntegerField(blank=True)),
                (
                    "emergency_contact_relation",
                    models.CharField(blank=True, max_length=100),
                ),
                ("my_file", models.FileField(blank=True, upload_to="doc")),
            ],
        ),
    ]
