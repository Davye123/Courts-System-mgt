# Generated by Django 4.2 on 2023-10-01 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('court_system', '0003_remove_case_enforcement_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lawyers',
            name='phone_number',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
