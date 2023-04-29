# Generated by Django 4.1.7 on 2023-04-17 08:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('Event', '0002_alter_representation_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Adresse mail de la reservation')),
                ('last_name', models.CharField(max_length=50, verbose_name='Nom de la personne qui a réserver')),
                ('first_name', models.CharField(max_length=50, verbose_name='Prénom de la personne qui réserve')),
                ('phone', models.CharField(max_length=10, verbose_name='Numéro de tel de la personne qui réserve')),
                ('date', models.DateTimeField(default=datetime.datetime(2023, 4, 17, 10, 58, 55, 750349), verbose_name='Date de la réservation')),
                ('note', models.CharField(max_length=1000, verbose_name='Remarque sur la réservation')),
                ('number', models.IntegerField(verbose_name='Numéro du ticket pour le spectatcle')),
                ('representation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.representation')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink_number', models.IntegerField(default=0, verbose_name='Ticket boisson pris avec la réservation')),
                ('food_number', models.IntegerField(default=0, verbose_name='Ticket nourriture pris avec la réservation')),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.price')),
                ('reservation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Reservation.reservation')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Event.place')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='SeatingTicket',
            fields=[
                ('ticket_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Reservation.ticket')),
                ('seat_number', models.CharField(max_length=3, verbose_name='Trigramme du siège')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('Reservation.ticket',),
        ),
        migrations.CreateModel(
            name='StandingTicket',
            fields=[
                ('ticket_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Reservation.ticket')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('Reservation.ticket',),
        ),
    ]