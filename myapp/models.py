from django.db import models

# 產品類型
class ProductType(models.Model):
    type_name = models.CharField(max_length=255)

    def __str__(self):
        return self.type_name

# 顏色
class Color(models.Model):
    color_name = models.CharField(max_length=100)

    def __str__(self):
        return self.color_name

# 尺寸
class Size(models.Model):
    size_name = models.CharField(max_length=50)

    def __str__(self):
        return self.size_name

# 產品
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.ForeignKey(ProductType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

# 產品圖片
class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image_url = models.URLField()

    def __str__(self):
        return f"Image for {self.product.name}"

# 庫存
class Inventory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Inventory for {self.product.name} - {self.color.color_name} - {self.size.size_name}"
