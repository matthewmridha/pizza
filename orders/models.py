from django.db import models

# Create your models here.
class Menu(models.Model):
    Catagory = (
        ("Pizza Regular", "PIZZA_REGULAR"),
        ("Pizza Sicilian", "PIZZA_SICILIAN"), 
        ("Subs", "SUB"), 
        ("Pasta", "PASTA"), 
        ("Salad", "SALAD"), 
        ("Dinner Plate", "DINNER_PLATE")
        )
    catagory = models.CharField(choices=Catagory, max_length=120)
    sub_catagory = models.CharField(max_length=120)
    small_price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=5)
    large_price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=5)
    regular_price = models.DecimalField(null=True, blank=True, decimal_places=2, max_digits=5)
    available = models.BooleanField(default=True, null=False)

    def __str__(self):
        if(self.available) == True:
            availability = "available"
        else:
            availability = "not available"
        return(f"{self.catagory} - {self.sub_catagory}, small={self.small_price}, large={self.large_price}, regular={self.regular_price} - {availability}")

class Topping(models.Model):
    topping = models.CharField(null=False, blank=False, max_length=120)
    available = models.BooleanField(default=True, null=False, blank=False)

    def __str__(self):
        if(self.available) == True:
            availability = "available"
        else:
            availability = "not available"
        return(f"{self.topping}, {availability}")
