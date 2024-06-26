# Generated by Django 5.0.6 on 2024-05-20 20:31

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=20)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('age', models.IntegerField()),
                ('location', models.CharField(default='', max_length=50)),
                ('parents_names', models.CharField(max_length=50)),
                ('fee_in_SHS', models.IntegerField()),
                ('brought_by', models.CharField(max_length=200)),
                ('baby_number', models.CharField(max_length=200, null=True, unique=True)),
                ('time_in', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Babypayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b_name', models.CharField(max_length=200)),
                ('paid_on', models.DateField(default=django.utils.timezone.now)),
                ('full_day', models.BooleanField(blank=True, default=False)),
                ('half_day', models.BooleanField(blank=True, default=False)),
                ('amount_due', models.DecimalField(blank=True, decimal_places=0, max_digits=15)),
                ('paid_amount', models.DecimalField(decimal_places=0, max_digits=15)),
                ('balance_left', models.DecimalField(blank=True, decimal_places=0, default=0, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='Doll_type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sitter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_name', models.CharField(max_length=20)),
                ('location', models.CharField(default='Kabalagala', max_length=20)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=10)),
                ('next_of_kin', models.CharField(max_length=20)),
                ('nin', models.CharField(max_length=20)),
                ('recommender_name', models.CharField(max_length=20)),
                ('religion', models.CharField(blank=True, max_length=25)),
                ('education_level', models.CharField(max_length=255)),
                ('sitter_number', models.CharField(max_length=8, null=True, unique=True)),
                ('contact', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Staytype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, related_name='customuser_groups', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='customuser_permissions', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Departure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_time', models.DateTimeField(auto_now_add=True)),
                ('picked_by', models.CharField(max_length=100)),
                ('comment', models.TextField(blank=True)),
                ('b_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daycare.baby')),
            ],
        ),
        migrations.CreateModel(
            name='Doll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doll_name', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity', models.IntegerField(default=0)),
                ('color', models.CharField(blank=True, max_length=200, null=True)),
                ('size', models.CharField(blank=True, max_length=200, null=True)),
                ('quantity_issued', models.IntegerField(blank=True, default=0, null=True)),
                ('quantity_received', models.IntegerField(blank=True, default=0, null=True)),
                ('unit_price', models.IntegerField(blank=True, default=0, null=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('t_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='daycare.doll_type')),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid_by', models.CharField(max_length=200, null=True)),
                ('quantity_sold', models.IntegerField(default=0)),
                ('received_amount', models.IntegerField(default=0)),
                ('date_sold', models.DateField(default=django.utils.timezone.now)),
                ('unit_price', models.IntegerField(default=0)),
                ('b_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daycare.baby')),
                ('doll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daycare.doll')),
            ],
        ),
        migrations.CreateModel(
            name='Sitterattendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sitter_number', models.CharField(max_length=200, unique=True)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(default='on-duty', max_length=15)),
                ('s_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daycare.sitter')),
            ],
        ),
        migrations.AddField(
            model_name='baby',
            name='assigned_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daycare.sitterattendance'),
        ),
        migrations.CreateModel(
            name='Sitterpayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('baby_count', models.IntegerField(default=0)),
                ('amount', models.IntegerField(default=3000)),
                ('total_amount', models.IntegerField(default=0)),
                ('s_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daycare.sitterattendance')),
            ],
        ),
        migrations.AddField(
            model_name='baby',
            name='period_of_stay',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daycare.staytype'),
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purchased_on', models.DateField(default=django.utils.timezone.now)),
                ('quantity_bought', models.IntegerField(default=0)),
                ('quantity_issued_out', models.IntegerField(default=0)),
                ('item_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='daycare.item')),
            ],
        ),
        migrations.CreateModel(
            name='Issuing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_to', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('issue_date', models.DateField()),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='daycare.stock')),
            ],
        ),
    ]
