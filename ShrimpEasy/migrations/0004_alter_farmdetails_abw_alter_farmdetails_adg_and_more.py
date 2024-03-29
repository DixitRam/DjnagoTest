# Generated by Django 5.0.2 on 2024-03-08 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ShrimpEasy', '0003_alter_farm_name_alter_farm_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='farmdetails',
            name='abw',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='farmdetails',
            name='adg',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='farmdetails',
            name='gain',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='farmdetails',
            name='weight',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='weatherreport',
            name='humidity',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='weatherreport',
            name='temperature',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
        migrations.AlterField(
            model_name='weatherreport',
            name='wind_speed',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]
