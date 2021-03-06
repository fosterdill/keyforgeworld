# Generated by Django 2.1.5 on 2019-01-20 23:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


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
                ('turn', models.IntegerField()),
                ('category', models.CharField(choices=[('Reap', 'REAP'), ('Fight', 'FIGHT'), ('Action', 'ACTION'), ('Play', 'PLAY')], max_length=6)),
                ('rank', models.IntegerField()),
                ('event_card_count', models.IntegerField()),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='card.Card')),
            ],
            options={
                'ordering': ('turn', 'rank'),
            },
        ),
        migrations.CreateModel(
            name='Synergy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('cards', models.ManyToManyField(through='synergy.Event', to='card.Card')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='synergy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='synergy.Synergy'),
        ),
    ]
