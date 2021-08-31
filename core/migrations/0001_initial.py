# Generated by Django 2.2.14 on 2021-08-25 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_categoria', models.CharField(max_length=100, verbose_name='Nome categoria')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['nome_categoria'],
            },
        ),
        migrations.CreateModel(
            name='Perdidos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomecompleto', models.CharField(max_length=45, verbose_name='Nome completo')),
                ('numero', models.CharField(max_length=30, verbose_name='Numero')),
                ('bairro', models.CharField(max_length=30, verbose_name='Bairro')),
                ('declarante', models.CharField(max_length=30, verbose_name='Declarante')),
                ('data_perdido', models.DateTimeField(verbose_name='Data')),
                ('date_registo', models.DateTimeField(auto_now_add=True)),
                ('photo1', models.ImageField(upload_to='itens_perdidos')),
                ('descricao', models.TextField(max_length=250, verbose_name='Descricao')),
                ('resolvido', models.BooleanField(default=False, verbose_name='Marcar como resolvido')),
                ('tipo_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipo_perdido', to='core.Categoria', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Perdido',
                'verbose_name_plural': 'Perdidos',
                'ordering': ['id', 'nomecompleto', 'data_perdido'],
            },
        ),
        migrations.CreateModel(
            name='Achados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomecompleto', models.CharField(max_length=45, verbose_name='Nome completo')),
                ('numero', models.CharField(max_length=30, verbose_name='Numero')),
                ('bairro', models.CharField(max_length=30, verbose_name='Bairro')),
                ('declarante', models.CharField(max_length=30, verbose_name='Declarante')),
                ('data_achado', models.DateTimeField(verbose_name='Data')),
                ('date_registo', models.DateTimeField(auto_now_add=True)),
                ('photo1', models.ImageField(upload_to='itens_perdidos')),
                ('descricao', models.TextField(max_length=250, verbose_name='Descricao')),
                ('resolvido', models.BooleanField(default=False, verbose_name='Marcar como resolvido')),
                ('tipo_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tipo_achados', to='core.Categoria', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Achado',
                'verbose_name_plural': 'Achados',
                'ordering': ['id', 'nomecompleto', 'data_achado'],
            },
        ),
    ]
