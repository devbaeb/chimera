# Generated by Django 4.0.4 on 2022-05-05 10:14

from django.db import migrations
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='note',
            field=wagtail.core.fields.RichTextField(default='def'),
            preserve_default=False,
        ),
    ]