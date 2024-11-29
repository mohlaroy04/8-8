from django.db import models


class FoodType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Food(models.Model):
    food_type = models.ForeignKey(FoodType, related_name='foods', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    ingredients = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.TextField()
    food = models.ForeignKey(Food, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.food.name}"