# Generated by Django 4.2.7 on 2023-11-25 12:35

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0004_remove_participante_equipe_equipe_membros"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="equipe",
            name="foto",
        ),
        migrations.RemoveField(
            model_name="equipe",
            name="nota",
        ),
    ]