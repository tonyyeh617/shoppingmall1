from django.core.management.base import BaseCommand

from myapp.models import ProductType, Color, Size, Product, ProductImage, Inventory

class Command(BaseCommand):
    help = '描述此命令的用途，例如處理某些數據'

    def handle(self, *args, **kwargs):
        # 建立產品類型
        type_shirt = ProductType.objects.create(type_name="Shirt")
        type_pants = ProductType.objects.create(type_name="Pants")

        # 建立顏色
        color_red = Color.objects.create(color_name="Red")
        color_blue = Color.objects.create(color_name="Blue")
        color_green = Color.objects.create(color_name="Green")

        # 建立尺寸
        size_s = Size.objects.create(size_name="S")
        size_m = Size.objects.create(size_name="M")
        size_l = Size.objects.create(size_name="L")

        # 建立產品
        product1 = Product.objects.create(
            name="Casual Shirt", 
            description="A comfortable casual shirt.", 
            price=29.99, 
            type=type_shirt
        )

        product2 = Product.objects.create(
            name="Formal Pants", 
            description="Elegant formal pants.", 
            price=49.99, 
            type=type_pants
        )

        # 建立產品圖片
        ProductImage.objects.create(product=product1, image_url="casual_shirt.jpg")
        ProductImage.objects.create(product=product2, image_url="formal_pants.jpg")

        # 建立庫存
        Inventory.objects.create(product=product1, color=color_red, size=size_s, quantity=10)
        Inventory.objects.create(product=product1, color=color_red, size=size_m, quantity=15)
        Inventory.objects.create(product=product1, color=color_blue, size=size_l, quantity=20)
        Inventory.objects.create(product=product2, color=color_green, size=size_s, quantity=5)
        Inventory.objects.create(product=product2, color=color_blue, size=size_m, quantity=8)
        Inventory.objects.create(product=product2, color=color_red, size=size_l, quantity=12)

        # 額外新增產品與庫存
        product3 = Product.objects.create(
            name="Summer T-Shirt", 
            description="Lightweight summer t-shirt.", 
            price=19.99, 
            type=type_shirt
        )

        ProductImage.objects.create(product=product3, image_url="summer_tshirt.jpg")
        Inventory.objects.create(product=product3, color=color_green, size=size_m, quantity=25)
        Inventory.objects.create(product=product3, color=color_blue, size=size_s, quantity=30)
