# Generated by Django 3.2.3 on 2021-06-01 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notebook', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='color',
            field=models.CharField(choices=[('a', 'yellow'), ('b', 'maroon'), ('c', 'lightseagreen'), ('d', 'red'), ('e', 'blue'), ('f', 'darkorange'), ('g', 'indigo')], default='a', max_length=1, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='note',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
