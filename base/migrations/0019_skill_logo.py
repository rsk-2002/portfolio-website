# Generated by Django 4.0.4 on 2022-04-17 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_alter_comment_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='logo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]