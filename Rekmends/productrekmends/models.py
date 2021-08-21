
from typing import Reversible
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from .utils import unique_slug_generator
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.urls import reverse
 
# Create your models here.

class categories(models.Model):
     name = models.CharField(default='', max_length=50, unique=True)

     def __str__(self):
        return self.name

class Post(models.Model):
    title=models.CharField(default='',max_length=200)
    image=models.ImageField(default='', upload_to='attachments/')
    decription=RichTextUploadingField()
    slug = models.SlugField(max_length=50, default='', blank=True)
    category=models.ForeignKey(
        categories, null=True, on_delete=models.CASCADE)
    subcategory=models.CharField(max_length=50, default='', blank=True)
    read=models.IntegerField(default=0)
    updated_on = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


    @staticmethod
    def get_all_product_by_category_id(category_name):
        if category_name:
            return Post.objects.filter(category__name=category_name)
        else:
            return Post.objects.all();  

    def get_category_name(self):
        return self.category.name

    def get_absolute_url(self):
        return reverse('blogdesc', args=[self.id,self.slug])

    
    
  
    

    def __str__(self):
        return self.title

    

@receiver(pre_save, sender=Post)
def update_Postslug(sender, instance, **kwargs):
    instance.title = instance.title.capitalize()
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)



class Review(models.Model):
    name = models.CharField(max_length=50,default='')
    email = models.EmailField(max_length=100, default='')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField(default='', max_length=1000)
    like=models.IntegerField(default=0)
    

    def __str__(self):
        return " {} {}(s).".format(self.email, self.post.title)

  

class Contact(models.Model):
    no=models.AutoField
    name=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    message=models.TextField(default="")
    timestamp=models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
       return self.name

class Product(models.Model):
    name=models.CharField(max_length=50,default='')
    image=models.ImageField(default='', upload_to='attachments/')
    description=models.TextField()
    category=models.ForeignKey(
        categories, null=True, on_delete=models.CASCADE)
    discount=models.CharField(max_length=50 ,default='',blank=True)
    oldprice=models.IntegerField()
    newprice=models.IntegerField()
    created_on= models.DateTimeField()
    product_link=models.URLField(max_length=500,default='')

    @staticmethod
    def get_all_product_by_category_name(category_name):
        if category_name:
            return Product.objects.filter(category__name=category_name)
        else:
            return Product.objects.all();  

    def __str__(self):
       return self.name

    

class subscribeform(models.Model):
    email=models.EmailField()

    def __str__(self):
       return self.email 



class coupon(models.Model):
    name=models.CharField(max_length=50,default='')
    description=models.TextField()
    code=models.CharField(max_length=50,default='')
    link=models.URLField(max_length=500,default='')
    created=models.DateTimeField(auto_now_add=True)
    status=models.BooleanField(default=True)
    def __str__(self):
       return self.name 