from django.db import models

# Create your models here.

class Pizza(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Topping(models.Model):
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = 'Toppings' ## I actually don't need this since it defaults by adding an 's'
    
    def __str__(self):
        return self.name