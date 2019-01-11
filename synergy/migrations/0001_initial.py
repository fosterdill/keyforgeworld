# Generated by Django 2.1.5 on 2019-01-11 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import synergy.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[(synergy.models.EventCategory('Reap'), 'Reap'), (synergy.models.EventCategory('Attack'), 'Attack'), (synergy.models.EventCategory('Action'), 'Action'), (synergy.models.EventCategory('Play'), 'Play')], max_length=6)),
                ('rank', models.IntegerField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.Card')),
            ],
        ),
        migrations.CreateModel(
            name='Synergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Turn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('cards', models.ManyToManyField(through='synergy.Event', to='card.Card')),
                ('synergy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='synergy.Synergy')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='turn',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='synergy.Turn'),
        ),
    ]
