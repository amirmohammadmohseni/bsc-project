# Generated by Django 3.0.7 on 2020-08-18 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0003_auto_20200818_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='defenseDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]