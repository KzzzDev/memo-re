# Generated by Django 3.2.16 on 2022-12-18 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(blank=True, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, verbose_name='username'),
        ),
    ]