# Generated by Django 4.0.4 on 2022-04-17 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_skill_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='logo',
            field=models.ImageField(default='R.png', null=True, upload_to=''),
        ),
    ]