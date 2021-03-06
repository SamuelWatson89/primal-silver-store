# Generated by Django 3.0.2 on 2020-01-26 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address_line1',
            field=models.CharField(blank=True, max_length=84, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address_line2',
            field=models.CharField(blank=True, max_length=84, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='country',
            field=models.CharField(blank=True, max_length=84, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='county',
            field=models.CharField(blank=True, max_length=84, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='postcode',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='town_city',
            field=models.CharField(blank=True, max_length=84, null=True),
        ),
    ]
