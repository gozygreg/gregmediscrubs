# Generated by Django 3.2 on 2023-04-02 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_testimonial'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]