# Generated by Django 3.0.7 on 2020-08-18 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proposals', '0002_comment_onproposal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='issuanceDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]