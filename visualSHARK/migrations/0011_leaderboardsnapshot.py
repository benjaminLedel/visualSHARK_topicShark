# Generated by Django 2.2.10 on 2020-04-02 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualSHARK', '0010_auto_20200401_1607'),
    ]

    operations = [
        migrations.CreateModel(
            name='LeaderboardSnapshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('data', models.TextField()),
            ],
        ),
    ]