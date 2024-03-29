# Generated by Django 4.0.6 on 2022-07-25 09:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_is_active_vendor'),
        ('product', '0004_order_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='vendor',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='accounts.vendor'),
            preserve_default=False,
        ),
    ]
