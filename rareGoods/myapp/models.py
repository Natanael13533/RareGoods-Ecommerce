from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from autoslug import AutoSlugField

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    category_slug = models.SlugField(unique=True)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "tbcategory"

    def __str__(self):
        return self.category_name

class Product(models.Model):
    product_name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='product_name', unique=True, always_update=True)
    description = models.TextField()
    pembelian = models.CharField(null=True, blank=True)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)

    image = models.ImageField(upload_to="product/images", default="")

    class Meta:
        db_table = "tbproduct"

    def __str__(self):
        return self.product_name

class Blog(models.Model):
    title = models.CharField(max_length=50)
    sub_description = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(default=timezone.now)

    image = models.ImageField(upload_to="blog/images", default="")

    class Meta:
        db_table = "tbblog"

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "tbcomment"

class Reply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    parent_comment = models.ForeignKey(Comment, on_delete=models.CASCADE, default=None)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "tbreply"

class Lokasi(models.Model):
    toko = models.CharField(max_length=200)
    kota = models.CharField(max_length=200)
    provinsi = models.CharField(max_length=150)
    alamat = models.CharField(max_length=300)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        db_table = "tblokasi"

    def __str__(self):
        return self.toko