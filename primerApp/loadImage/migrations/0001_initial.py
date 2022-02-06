# Generated by Django 4.0.1 on 2022-02-06 08:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImgTableModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_img', models.CharField(max_length=255, null=True)),
                ('format_img', models.CharField(max_length=40, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('edit', models.DateTimeField(blank=True, default=None, null=True)),
                ('url_img', models.ImageField(upload_to='img/',null=False)),
            ],
            options={
                'db_table': 'imgTable',
            },
        ),
    ]
