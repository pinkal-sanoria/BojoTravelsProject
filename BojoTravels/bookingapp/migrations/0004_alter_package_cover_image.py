# Generated by Django 4.0.5 on 2023-03-10 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0003_alter_package_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='package',
            name='cover_image',
            field=models.ImageField(blank=True, null=True, upload_to='package_images/'),
        ),
    ]