# Generated by Django 3.1.1 on 2020-09-12 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C1', models.CharField(max_length=20, null=True)),
                ('C2', models.CharField(max_length=20, null=True)),
                ('name', models.CharField(max_length=20, null=True)),
                ('sum', models.IntegerField(default=0)),
                ('stock', models.IntegerField(default=0)),
                ('using', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=20, null=True)),
                ('user', models.TextField(null=True)),
                ('number', models.TextField(null=True)),
                ('date', models.TextField(null=True)),
                ('back_or_not', models.TextField(null=True)),
            ],
        ),
    ]