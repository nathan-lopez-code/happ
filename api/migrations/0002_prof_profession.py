# Generated by Django 3.2.16 on 2023-07-26 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prof',
            name='profession',
            field=models.CharField(blank=True, default='professeur ordinaire', max_length=100, null=True),
        ),
    ]
