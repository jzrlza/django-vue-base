# Generated by Django 2.1.4 on 2018-12-25 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('myuser_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]