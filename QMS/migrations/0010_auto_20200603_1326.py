# Generated by Django 3.0 on 2020-06-03 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QMS', '0009_auto_20200530_1925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Postpond',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auditschedule_id', models.IntegerField(null=True)),
                ('post_date', models.DateField(null=True)),
                ('post_time', models.TimeField(null=True)),
                ('reason', models.TextField(null=True)),
                ('status', models.CharField(max_length=10, null=True)),
            ],
            options={
                'db_table': 'postpond',
            },
        ),
        migrations.RemoveField(
            model_name='jobdetails',
            name='client_name',
        ),
        migrations.RemoveField(
            model_name='jobdetails',
            name='end_user',
        ),
        migrations.RemoveField(
            model_name='jobdetails',
            name='job_type',
        ),
        migrations.DeleteModel(
            name='ClientName',
        ),
        migrations.DeleteModel(
            name='EndUser',
        ),
        migrations.DeleteModel(
            name='JobDetails',
        ),
        migrations.DeleteModel(
            name='JobType',
        ),
    ]
