from django.db import models
from .utils import unique_slug_generator
from django.db.models.signals import pre_save, post_save

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.FileField(upload_to='product/', null=True, blank=True)



    def get_absolute_url(self):
        return "/product/{slug}/".format(slug=self.slug)
        return reversed("product:productlist", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title

def product_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(product_pre_save_reciever, sender=Product)