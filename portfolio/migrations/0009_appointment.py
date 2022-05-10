# Generated by Django 4.0.2 on 2022-02-22 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_choose_class_name_icon_alter_choose_class_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='appointment_images', verbose_name='Upload an Image for Appointment Section')),
                ('heading_one', models.CharField(blank=True, max_length=50, null=True, verbose_name='Write a Heading For First Card')),
                ('description_one', models.CharField(blank=True, max_length=200, null=True, verbose_name='Write a Description For First Card')),
                ('heading_two', models.CharField(blank=True, max_length=50, null=True, verbose_name='Write a Heading For Second Card')),
                ('description_two', models.CharField(blank=True, max_length=200, null=True, verbose_name='Write a Description For Second Card')),
                ('number', models.IntegerField(default=0, verbose_name='Enter Number For Appointment')),
                ('check_point_one', models.CharField(blank=True, max_length=50, null=True, verbose_name='Write a First Check Point')),
                ('check_point_two', models.CharField(blank=True, max_length=50, null=True, verbose_name='Write a Second Check Point')),
                ('check_point_three', models.CharField(blank=True, max_length=50, null=True, verbose_name='Write a Third Check Point')),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Appointment',
                'verbose_name_plural': 'Appointments',
            },
        ),
    ]