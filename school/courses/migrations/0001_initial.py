# Generated by Django 3.2.12 on 2024-04-15 02:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.DateTimeField(default=True)),
                ('tittle', models.CharField(max_length=255)),
                ('url', models.URLField(unique=True)),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='Avaliable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('active', models.DateTimeField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('comments', models.TextField(blank=True, default='')),
                ('avaliable', models.DecimalField(decimal_places=1, max_digits=2)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliables', to='courses.course')),
            ],
            options={
                'verbose_name': 'Avaliable',
                'verbose_name_plural': 'Avaliables',
                'unique_together': {('email', 'course')},
            },
        ),
    ]
