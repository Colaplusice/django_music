# Generated by Django 2.2.10 on 2020-06-30 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20200628_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='userword',
            name='learned',
            field=models.BooleanField(default=True, verbose_name='是否掌握'),
            preserve_default=False,
        ),
    ]