# Generated by Django 3.1.6 on 2021-02-05 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=16, verbose_name='Name')),
                ('car_model', models.CharField(max_length=16, verbose_name='Model')),
                ('car_class', models.CharField(choices=[('premium', 'Premium'), ('hatchback', 'Hatchback'), ('city_cars', 'Small Car'), ('mpv', 'MPV'), ('van', 'Cargo Van')], max_length=32, verbose_name='Car class')),
                ('body_type', models.CharField(choices=[('limusine', 'Limusine'), ('combi', 'Combi')], max_length=32, verbose_name='Body type')),
                ('engine_type', models.CharField(choices=[('diesel', 'Diesel'), ('petrol', 'Petrol'), ('fullhybrid', 'FullHybrid'), ('semihybrid', 'SemiHybrid'), ('electric', 'Electric')], max_length=32, verbose_name='Engine Type')),
                ('eng_capicity', models.DecimalField(decimal_places=1, max_digits=2, verbose_name='Engine capicity')),
                ('hp', models.IntegerField(default=None, verbose_name='Horse power:')),
                ('d_production', models.DateField(default=None, verbose_name='Date of production')),
                ('reg_plates', models.CharField(max_length=8, unique=True, verbose_name='Registration Plates')),
                ('vin', models.CharField(max_length=14, unique=True, verbose_name='Vin')),
                ('millage', models.IntegerField(verbose_name='millage')),
                ('next_service', models.IntegerField(verbose_name='Next service at millage')),
                ('car_inspection', models.DateField(verbose_name='Car inspection valifation date')),
                ('insurence', models.DateField(verbose_name='Car insurence validation date')),
                ('p_capicity', models.IntegerField(verbose_name='Number of seats')),
                ('num_of_doors', models.IntegerField(verbose_name='Number of doors')),
                ('damage', models.CharField(choices=[('free_of_damages', 'Free of damages'), ('damaged', 'Damaged')], max_length=32, verbose_name='Damages')),
                ('status', models.CharField(choices=[('free', 'Free'), ('service', 'In Service'), ('torefuel', 'To refuel'), ('needwash', 'Need wash'), ('booked', 'Booked'), ('blocked', 'Blocked')], default='free', max_length=32, verbose_name='Car Status')),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=32, verbose_name='name')),
                ('surname', models.CharField(default=None, max_length=32, verbose_name='surname')),
                ('strname', models.CharField(default=None, max_length=32, verbose_name='street name')),
                ('homenum', models.CharField(default=None, max_length=32, verbose_name='home number')),
                ('flatnum', models.IntegerField(blank=True, null=True, verbose_name='flat number')),
                ('idnum', models.CharField(default=None, max_length=9, unique=True, verbose_name='ID number')),
                ('dlnum', models.CharField(default=None, max_length=12, unique=True, verbose_name='Drivin licens number')),
                ('pesel', models.BigIntegerField(default=None, unique=True, verbose_name='Pesel')),
                ('email', models.CharField(max_length=32, unique=True, verbose_name='e-mail')),
                ('phonenum', models.IntegerField(unique=True, verbose_name='phone number')),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Start of rent')),
                ('end_date', models.DateField(verbose_name='End of rent')),
                ('start_millage', models.IntegerField(default=None)),
                ('end_millage', models.IntegerField(default=None)),
                ('millage_done', models.IntegerField(default=None)),
                ('reservation_status', models.CharField(default='Unconfirmed', max_length=16)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_rental_app.car')),
                ('driver', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='car_rental_app.client')),
            ],
        ),
        migrations.CreateModel(
            name='ReservationOptions',
            fields=[
                ('reservation', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='car_rental_app.reservation')),
                ('child_seat', models.CharField(blank=True, choices=[('e', '-----------'), ('a', '0-9kg'), ('b', '9-18kg'), ('c', '18-36kg'), ('d', 'pad')], max_length=32, verbose_name='Choose child seats:')),
                ('number_of_cs', models.IntegerField(blank=True, verbose_name='Number of child seats')),
                ('additional_driver', models.CharField(choices=[('YES', 'yes'), ('NO', 'no')], max_length=32, verbose_name='Additional driver')),
                ('abolition', models.CharField(choices=[('YES', 'yes'), ('NO', 'no')], max_length=32, verbose_name='Abolition')),
                ('insurence', models.CharField(blank=True, choices=[('standard', 'Standard'), ('extended', 'Extended')], default=None, max_length=32, verbose_name='Choose type of insurence')),
            ],
        ),
        migrations.CreateModel(
            name='ClientAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='Start of rent')),
                ('end_date', models.DateField(verbose_name='End of rent')),
                ('child_seat', models.CharField(blank=True, choices=[('e', '-----------'), ('a', '0-9kg'), ('b', '9-18kg'), ('c', '18-36kg'), ('d', 'pad')], default='None', max_length=32, verbose_name='Choose child seats:')),
                ('number_of_cs', models.IntegerField(blank=True, default=0, verbose_name='Number of child seats')),
                ('additional_driver', models.CharField(choices=[('YES', 'yes'), ('NO', 'no')], default='no', max_length=32, verbose_name='Additional driver')),
                ('abolition', models.CharField(choices=[('YES', 'yes'), ('NO', 'no')], default='no', max_length=32, verbose_name='Abolition')),
                ('insurence', models.CharField(blank=True, choices=[('standard', 'Standard'), ('extended', 'Extended')], max_length=32, verbose_name='Choose type of insurence')),
                ('name', models.CharField(blank=True, max_length=32, verbose_name='name')),
                ('surname', models.CharField(blank=True, max_length=32, verbose_name='surname')),
                ('email_q', models.CharField(blank=True, max_length=32, verbose_name='e-mail')),
                ('phonenum_q', models.IntegerField(blank=True, default=0, verbose_name='phone number')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_rental_app.car')),
            ],
        ),
        migrations.CreateModel(
            name='CarDamage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date of accident')),
                ('d_status', models.CharField(choices=[('reapaird', 'Reapaird'), ('unreapaird', 'Unreapaird')], default='repaird', max_length=16)),
                ('title', models.CharField(default=None, max_length=64, verbose_name='Title')),
                ('d_type', models.CharField(choices=[('body', 'Body'), ('engine', 'Engine'), ('electric', 'Electric'), ('chasis', 'Chasis')], default=None, max_length=128)),
                ('d_note', models.TextField(default=None, verbose_name='Damages description')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='car_rental_app.car')),
                ('driver', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='car_rental_app.client')),
            ],
        ),
    ]