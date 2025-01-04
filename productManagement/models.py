from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.URLField(max_length=2083)
    category =models.CharField(max_length=255)
    # category = models.ForeignKey(
    #     Category, related_name="products", on_delete=models.CASCADE
    # )



    def __str__(self):
        return self.name

