# Generated by Django 2.2.13 on 2020-07-01 09:27

from django.db import migrations, models
import django.db.models.manager
import django_handleref.models
import django_inet.models


class Migration(migrations.Migration):

    dependencies = [
        ('peeringdb_server', '0036_ixlanprefix_in_dfz'),
    ]

    operations = [
        migrations.CreateModel(
            name='IXFMemberData',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, max_length=255, verbose_name='Status')),
                ('created', django_handleref.models.CreatedDateTimeField(auto_now_add=True, verbose_name='Created')),
                ('updated', django_handleref.models.UpdatedDateTimeField(auto_now=True, verbose_name='Updated')),
                ('version', models.IntegerField(default=0)),
                ('asn', django_inet.models.ASNField()),
                ('ipaddr4', django_inet.models.IPAddressField(blank=True, max_length=39, null=True)),
                ('ipaddr6', django_inet.models.IPAddressField(blank=True, max_length=39, null=True)),
                ('is_rs_peer', models.BooleanField(default=False)),
                ('notes', models.CharField(blank=True, max_length=255)),
                ('speed', models.PositiveIntegerField()),
                ('operational', models.BooleanField(default=True)),
                ('data', models.TextField(default='{}', help_text='JSON snapshot of the ix-f member data that created this conflict')),
            ],
            options={
                'db_table': 'peeringdb_ixf_data_conflict',
            },
            managers=[
                ('handleref', django.db.models.manager.Manager()),
            ],
        ),
    ]
