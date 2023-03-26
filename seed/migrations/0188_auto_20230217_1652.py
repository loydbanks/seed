# Generated by Django 3.2.17 on 2023-02-16 20:43

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0187_update_compliance_metric_cycles'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('cycle', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='seed.cycle')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='seed.property')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NoteEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='seed.event')),
                ('note', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seed.note')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
            bases=('seed.event',),
        ),
        migrations.CreateModel(
            name='ATEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='seed.event')),
                ('building_file', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='seed.buildingfile')),
                ('audit_date', models.CharField(max_length=100, null=True)),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
            bases=('seed.event',),
        ),
        migrations.CreateModel(
            name='AnalysisEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='seed.event')),
                ('analysis', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seed.analysis')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
            bases=('seed.event',),
        ),
        migrations.AddField(
            model_name='scenario',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='scenarios', to='seed.atevent'),
        ),
    ]
