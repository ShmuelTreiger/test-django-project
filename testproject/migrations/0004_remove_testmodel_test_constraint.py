# Generated by Django 4.0 on 2021-12-07 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testproject', '0003_testmodel_test_constraint'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='testmodel',
            name='test_constraint',
        ),
    ]
