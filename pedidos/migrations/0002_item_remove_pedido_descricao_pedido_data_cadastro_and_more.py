# Generated by Django 4.2.3 on 2024-09-19 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('preco', models.FloatField()),
                ('descricao', models.CharField(max_length=100)),
                ('estabelecimento', models.CharField(max_length=100)),
                ('observacao', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='descricao',
        ),
        migrations.AddField(
            model_name='pedido',
            name='data_cadastro',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='valor_total',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='pedido',
            name='item',
            field=models.ManyToManyField(to='pedidos.item'),
        ),
    ]
