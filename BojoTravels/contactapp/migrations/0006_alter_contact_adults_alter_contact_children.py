# Generated by Django 4.0.5 on 2023-03-15 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactapp', '0005_alter_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='adults',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='children',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
