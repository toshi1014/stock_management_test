# Generated by Django 3.1.1 on 2020-09-15 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='C1',
            field=models.TextField(choices=[('MISUMI', 'MISUMI'), ('電気系', '電気系')], null=True),
        ),
    ]