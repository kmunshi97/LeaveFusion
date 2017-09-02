# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 07:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentLeaveRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission', models.CharField(default='other', max_length=20)),
                ('station', models.BooleanField(default=False)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cur_leave_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Leave',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_leave', models.CharField(choices=[('casual', 'Casual Leave'), ('restricted', 'Restricted Holidays'), ('vacation', 'Vacation Leave'), ('commuted', 'Commuted Leave'), ('earned', 'Earned Leave'), ('special_casual', 'Special Casual Leave')], default='casual', max_length=20)),
                ('acad_done', models.BooleanField(default=True)),
                ('admin_done', models.BooleanField(default=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('purpose', models.CharField(default='No Purpose', max_length=1000)),
                ('leave_address', models.CharField(blank=True, default='', max_length=100)),
                ('status', models.CharField(default='processing', max_length=10)),
                ('station', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('academic_replacement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='acad_rep_for', to=settings.AUTH_USER_MODEL)),
                ('administrative_replacement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin_rep_for', to=settings.AUTH_USER_MODEL)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leave_applications', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeaveRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.CharField(default='', max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('station', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='leave_requests', to=settings.AUTH_USER_MODEL)),
                ('leave', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='leave_application.Leave')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.Designation')),
                ('requested_from', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='received_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='LeavesCount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('casual', models.IntegerField(default=8)),
                ('special_casual', models.IntegerField(default=15)),
                ('restricted', models.IntegerField(default=2)),
                ('commuted', models.IntegerField(default=20)),
                ('earned', models.IntegerField(default=30)),
                ('vacation', models.IntegerField(default=60)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='currentleaverequest',
            name='leave',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cur_requests', to='leave_application.Leave'),
        ),
        migrations.AddField(
            model_name='currentleaverequest',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.Designation'),
        ),
        migrations.AddField(
            model_name='currentleaverequest',
            name='requested_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cur_received_requests', to=settings.AUTH_USER_MODEL),
        ),
    ]
