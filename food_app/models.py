from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=125)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return f"{self.name}"




class Food(models.Model):
    name = models.CharField(max_length=125)
    description = models.CharField(max_length=400)
    price = models.IntegerField()
    image = models.ImageField(upload_to='food_images/')
    category = models.ForeignKey(Category, related_name='category_food', on_delete=models.CASCADE)
    is_active = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Food'
        ordering = ['name']

    def __str__(self):
        return f"{self.name} {self.description}"
