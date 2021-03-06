# Generated by Django 2.0.7 on 2018-09-06 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CSI_Web', '0002_auto_20180830_0131'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('problem_category', models.CharField(max_length=100)),
                ('problem_description', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=30)),
                ('contact_number', models.CharField(max_length=15)),
                ('contact_address', models.CharField(max_length=100)),
                ('email_id', models.EmailField(max_length=254)),
            ],
        ),
    ]
