# Generated by Django 4.2 on 2024-09-29 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects_info', '0002_myinfo_alter_projectsinfo_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectsinfo',
            name='github',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='projectsinfo',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='technologies',
            name='image',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
