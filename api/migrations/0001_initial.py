# Generated by Django 2.1.1 on 2018-09-12 14:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('start_amount', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(default=None, upload_to='pic_folder/')),
                ('start_time', models.DateField(default=django.utils.timezone.now)),
                ('end_time', models.DateField(default=django.utils.timezone.now)),
                ('winner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_by_user', models.IntegerField(blank=True, null=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.AuctionItem')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
