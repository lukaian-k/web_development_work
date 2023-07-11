# Generated by Django 4.2.2 on 2023-07-11 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_dispositivoseletronicos_saladeaula'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alocacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sala', models.CharField(choices=[('Sala 1', 'Sala 1'), ('Sala 2', 'Sala 2')], max_length=100)),
                ('bloco', models.CharField(choices=[('Bloco 1', 'Bloco 1'), ('Bloco 2', 'Bloco 2')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('departamento', models.CharField(max_length=100)),
                ('codigo', models.CharField(max_length=10)),
                ('formacao', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sala',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='saladeaula',
            name='DispositivosEletronicos',
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='DispositivosEletronicos',
        ),
        migrations.DeleteModel(
            name='SaladeAula',
        ),
        migrations.AddField(
            model_name='alocacao',
            name='curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.curso'),
        ),
        migrations.AddField(
            model_name='alocacao',
            name='professor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.professor'),
        ),
    ]
