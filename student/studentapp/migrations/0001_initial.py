# Generated by Django 4.0.5 on 2022-07-02 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('department', models.TextField()),
                ('email', models.CharField(max_length=250)),
                ('mobile', models.IntegerField()),
                ('address', models.TextField()),
            ],
        ),
    ]
