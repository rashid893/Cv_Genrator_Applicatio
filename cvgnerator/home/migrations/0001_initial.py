# Generated by Django 4.0.3 on 2022-03-20 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=44)),
                ('email', models.CharField(max_length=44)),
                ('phone', models.CharField(max_length=44)),
                ('summary', models.TextField(max_length=1184)),
                ('degree', models.CharField(max_length=44)),
                ('school', models.CharField(max_length=44)),
                ('uinversity', models.CharField(max_length=44)),
                ('previous', models.TextField(max_length=1244)),
                ('skills', models.TextField(max_length=1244)),
            ],
        ),
    ]