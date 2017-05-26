from django.db import models


class Recipe(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.ManyToManyField("recipes.Ingredient", through="recipes.RecipeIngredient")
    instructions = models.TextField()


class Ingredient(models.Model):
    name = models.CharField(max_length=200)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)



