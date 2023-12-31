# Generated by Django 4.2.3 on 2023-08-01 16:46

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('action', '0001_initial'),
        ('organisation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Suggestions',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('content', models.JSONField(default=dict, help_text='{"language": "en", "content_data": "Some content"}')),
                ('count', models.PositiveIntegerField(default=0)),
                ('action', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='action.action')),
                ('organisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organisation.organisation')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
