# Generated by Django 2.2.2 on 2019-11-22 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_remove_student_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.IntegerField(null=True),
        ),
    ]
