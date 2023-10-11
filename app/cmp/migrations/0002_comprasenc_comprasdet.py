# Generated by Django 4.2.5 on 2023-10-11 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inv', '0005_producto'),
        ('cmp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComprasEnc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('fecha_compra', models.DateField(blank=True, null=True)),
                ('observacion', models.TextField(blank=True, null=True)),
                ('no_factura', models.CharField(max_length=100)),
                ('fecha_factura', models.DateField()),
                ('sub_total', models.FloatField(default=0)),
                ('descuento', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmp.proveedor')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Encabezado Compra',
                'verbose_name_plural': 'Encabezado Compras',
            },
        ),
        migrations.CreateModel(
            name='ComprasDet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('fc', models.DateTimeField(auto_now_add=True)),
                ('fm', models.DateTimeField(auto_now=True)),
                ('um', models.IntegerField(blank=True, null=True)),
                ('cantidad', models.BigIntegerField(default=0)),
                ('precio_prv', models.FloatField(default=0)),
                ('sub_total', models.FloatField(default=0)),
                ('descuento', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('costo', models.FloatField(default=0)),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cmp.comprasenc')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inv.producto')),
                ('uc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Detalle Compra',
                'verbose_name_plural': 'Detalles Compras',
            },
        ),
    ]
