# Generated by Django 4.0 on 2021-12-07 23:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testproject', '0004_remove_testmodel_test_constraint'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='testmodel',
            unique_together={('x', 'y')},
        ),
    ]