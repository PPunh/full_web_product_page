# coding=utf-8
from django.db import models

class ProductsCategory(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_name = models.CharField(max_length=50)
    category_descriptions = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'category'
        ordering = ('category_id',)

    def __str__(self):
        return f"{self.category_name} {self.category_descriptions}"


class ProductsModel(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_category = models.ForeignKey(
        ProductsCategory,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='product'
    )
    product_name = models.CharField(max_length=60)
    product_description = models.TextField(blank=True, null=True)
    product_pricing = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='products/', blank=True, null=True)
    product_created_at = models.DateTimeField(auto_now_add=True)
    product_updated_at = models.DateTimeField(auto_now=True)
    product_is_premium = models.BooleanField(default=False)
    product_show_in_homepage = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['product_name']
    
    def __str__(self):
        return f"{self.product_id} - {self.product_name} - {self.product_pricing} - {self.product_is_premium}"
