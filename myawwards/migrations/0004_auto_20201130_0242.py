# Generated by Django 3.1.3 on 2020-11-29 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myawwards', '0003_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=300),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.TextField(max_length=30),
        ),
    ]
