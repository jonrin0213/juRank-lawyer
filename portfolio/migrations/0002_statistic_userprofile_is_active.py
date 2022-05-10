# Generated by Django 4.0.2 on 2022-02-20 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Statistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_case', models.IntegerField(default=0)),
                ('active_case', models.IntegerField(default=0)),
                ('successful', models.IntegerField(default=0)),
                ('awards', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Statistic',
                'verbose_name_plural': 'Statistics',
            },
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]