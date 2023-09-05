# Generated by Django 4.2 on 2023-05-27 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_alter_projects_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_updated', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(default='', max_length=20)),
                ('type', models.CharField(default='stack', max_length=20)),
                ('proficency', models.CharField(default='Intermediate+', max_length=20)),
                ('score', models.IntegerField(default=60)),
                ('logo', models.CharField(max_length=4000)),
            ],
        ),
        migrations.DeleteModel(
            name='Tech_Stacks',
        ),
    ]