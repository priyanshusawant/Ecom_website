from django.db import models

# Create your models here.


class Item(models.Model):
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