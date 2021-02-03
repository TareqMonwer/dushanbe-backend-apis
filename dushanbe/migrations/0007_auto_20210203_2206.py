# Generated by Django 3.1.2 on 2021-02-03 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dushanbe', '0006_auto_20210203_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_serial_no', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('unit', models.CharField(blank=True, max_length=10, null=True)),
                ('quantity', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('submission_date', models.DateField(auto_now_add=True, null=True)),
                ('work_progress', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('bill', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nameofwork_bill', to='dushanbe.bill')),
                ('material', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='nameofwork_material', to='dushanbe.material')),
            ],
            options={
                'verbose_name_plural': 'Works',
            },
        ),
        migrations.CreateModel(
            name='WorkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('work_type_name', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name_plural': 'Work Types',
            },
        ),
        migrations.DeleteModel(
            name='NameOfWork',
        ),
        migrations.AddField(
            model_name='work',
            name='work_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='nameofwork_work_type', to='dushanbe.worktype'),
        ),
    ]
