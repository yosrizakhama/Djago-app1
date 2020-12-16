# Generated by Django 3.1.4 on 2020-12-14 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, null=True)),
                ('last_name', models.CharField(max_length=30, null=True)),
                ('email', models.CharField(max_length=50, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('age', models.IntegerField(null=True)),
            ],
        ),
    ]
