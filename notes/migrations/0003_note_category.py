# Generated by Django 2.0.6 on 2018-06-26 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_personalnote'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='category',
            field=models.CharField(default='default', max_length=20),
            preserve_default=False,
        ),
    ]