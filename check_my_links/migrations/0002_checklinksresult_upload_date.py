# Generated by Django 3.1.3 on 2021-01-25 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('check_my_links', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='checklinksresult',
            name='upload_date',
            field=models.DateField(auto_now=True),
        ),
    ]
