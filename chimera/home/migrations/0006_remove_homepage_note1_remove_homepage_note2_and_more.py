# Generated by Django 4.0.4 on 2022-05-05 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_note_homepage_note1_homepage_note2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='note1',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='note2',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='note3',
        ),
    ]