# Generated by Django 5.0 on 2023-12-19 08:06

import froala_editor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=1000)),
                ('contents', froala_editor.fields.FroalaField()),
                ('slug', models.SlugField(max_length=1000)),
                ('publication_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
