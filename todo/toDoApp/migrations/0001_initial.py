# Generated by Django 4.1.4 on 2023-02-05 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('is_done', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
