# Generated by Django 3.0.11 on 2020-12-15 16:20

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Constant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('version', models.PositiveSmallIntegerField(default=1)),
                ('identifier', models.CharField(max_length=64)),
                ('value', models.FloatField()),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='actions.Action')),
            ],
            options={
                'unique_together': {('action', 'version', 'identifier')},
            },
        ),
    ]
