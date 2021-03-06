# Generated by Django 3.1.6 on 2021-08-17 14:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Respondent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('email_address', models.CharField(max_length=200)),
                ('street', models.CharField(max_length=200)),
                ('barangay', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('contact', models.IntegerField()),
                ('city', models.CharField(max_length=200)),
                ('zip_code', models.IntegerField()),
                ('image', models.ImageField(blank=True, default='default.png', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('Student', 'Student'), ('Faculty', 'Faculty'), ('Admin', 'Admin'), ('Others', 'Others')], max_length=200)),
                ('vaccines', models.CharField(choices=[('AstraZeneca', 'AstraZeneca'), ('Pfizer', 'Pfizer'), ('Moderna', 'Moderna'), ('Sputnik V', 'Sputnik V'), ('Covaxin', 'Covaxin'), ('CoronaVac', 'CoronaVac'), ('Johnson & Johnson', 'Johnson & Johnson')], max_length=200)),
                ('how_many_times_have_you_been_injected_by_vaccine', models.CharField(choices=[('One', 'One'), ('Two', 'Two')], max_length=200)),
                ('dose', models.CharField(max_length=20)),
                ('where_did_you_get_the_vaccine', models.CharField(max_length=50)),
                ('date_attended', models.DateTimeField()),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('comments', models.TextField(blank=True, default='none', max_length=200, null=True)),
                ('person', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='nurse.respondent')),
            ],
        ),
    ]
