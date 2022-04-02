# Generated by Django 2.2.16 on 2022-03-31 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20220331_1827'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favoriterecipe',
            options={'verbose_name': 'Избранное', 'verbose_name_plural': 'Избранное'},
        ),
        migrations.AlterModelOptions(
            name='ingredient',
            options={'verbose_name': 'Ингредиенты', 'verbose_name_plural': 'Ингредиенты'},
        ),
        migrations.AlterModelOptions(
            name='ingredientsamount',
            options={'verbose_name': 'Количество ингредиентов', 'verbose_name_plural': 'Количество ингредиентов'},
        ),
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['-id'], 'verbose_name': 'Рецепты', 'verbose_name_plural': 'Рецепты'},
        ),
        migrations.AlterModelOptions(
            name='recipetag',
            options={'verbose_name': 'Тэги рецепта', 'verbose_name_plural': 'Тэги рецепта'},
        ),
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={'verbose_name': 'Список покупок', 'verbose_name_plural': 'Список покупок'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Теги', 'verbose_name_plural': 'Теги'},
        ),
    ]