# Generated by Django 2.2.16 on 2022-04-03 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20220403_1606'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='favoriterecipe',
            name='unique_recipe_user',
        ),
        migrations.RemoveConstraint(
            model_name='shoppingcart',
            name='unique_recipe_user',
        ),
        migrations.AddConstraint(
            model_name='favoriterecipe',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='unique_fav_recipe_user'),
        ),
        migrations.AddConstraint(
            model_name='shoppingcart',
            constraint=models.UniqueConstraint(fields=('user', 'recipe'), name='unique_sc_recipe_user'),
        ),
    ]