# Generated by Django 4.1.13 on 2025-02-10 09:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("innovatex", "0002_alter_blogpost_options_alter_casestudy_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="client",
            options={
                "ordering": ["-created_at"],
                "verbose_name": "Client",
                "verbose_name_plural": "Clients",
            },
        ),
        migrations.RenameField(
            model_name="client",
            old_name="clinet_logo",
            new_name="client_logo",
        ),
    ]
