# Generated by Django 2.2 on 2020-06-04 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0011_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='empPosition',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='empName',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='empTel',
            field=models.IntegerField(null=True),
        ),
    ]
