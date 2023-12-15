from django.db import models
from django.contrib.auth.models import User

# Create your models here.

category_choices = (
    ('CR','Curd'),
    ('ML','Milk'),
    ('PN','Paneer'),
    ('MS','Milkshake'),
    ('BT','Butter'),
    ('CZ','Cheese'),
    ('IC','Ice Creams'),
    ('GH','Ghee'),
    ('LS','Lassi'),
)

class Item(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        default = '1'
    )
    prod_code = models.IntegerField(default=100)
    for_user = models.CharField(
        max_length=100,
        default='xyz'
    )
    item_name = models.CharField(max_length=  50)
    item_desc = models.CharField(
        max_length = 300,
        default='''Lorem, ipsum dolor sit amet consectetur adipisicing elit. A nam voluptate assumenda recusandae officia et
        consequatur,nobis voluptatem incidunt laborum harum doloribus aspernatur iure aperiam adipisci quas alias ea delectus!'''
    )
    item_price = models.IntegerField()
    category = models.CharField(choices=category_choices, max_length=2, null=True)
    item_img = models.CharField(
        max_length=500,
        default="https://static.vecteezy.com/system/resources/previews/003/170/825/original/isolated-food-plate-fork-and-spoon-design-free-vector.jpg"
    )


    def __str__(self):
        return self.item_name
    
class HISTORY(models.Model):

    user_name = models.CharField(max_length=100)
    prod_ref = models.IntegerField(default=100)
    item_name = models.CharField(max_length=200)
    op_type = models.CharField(max_length=100)

    def __str__(self):
        return str(
            (
                self.prod_ref,
                self.user_name,
                self.item_name,
                self.op_type
            )
        )
    

class Cart(models.Model):

    order_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)