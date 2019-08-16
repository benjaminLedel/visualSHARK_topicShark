# Generated by Django 2.2.4 on 2019-08-16 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualSHARK', '0008_issuevalidation_issuevalidationuser'),
    ]

    operations = [
        migrations.CreateModel(
            name='RightsSupport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': (('view_issue_link', 'View issue links rights'), ('edit_issue_link', 'Edit issue links rights'), ('view_issue_labels', 'View issue labels rights'), ('edit_issue_labels', 'Edit issue labels rights'), ('view_issue_conflicts', 'View issue label conflict right'), ('edit_issue_conflicts', 'View issue label conflict right')),
                'managed': False,
            },
        ),
    ]