# Generated by Django 4.1.13 on 2025-02-27 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("innovatex", "0004_jobposition_jobapplication"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobapplication",
            name="job",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="applications",
                to="innovatex.jobposition",
            ),
        ),
    ]
