# Generated by Django 4.2.2 on 2024-04-28 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Community', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='status',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]