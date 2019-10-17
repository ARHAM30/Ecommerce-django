from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.FileField(upload_to='product/', null=True, blank=True)


    # object = ProductManager()

    def get_absolute_url(self):
        return "/product/{slug}/".format(slug=self.slug)

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
