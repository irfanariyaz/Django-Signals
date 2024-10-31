import datetime
import threading
from time import sleep

from django.utils import timezone

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.text import slugify
# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published',null=True,blank=True)
    slug = models.SlugField(max_length=200, unique=True,null=True,blank=True)
    body = models.TextField()

@receiver(pre_save, sender=Blog)
def pre_save_blog(sender, instance, **kwargs):
    print("Handler function Thread Id-", threading.get_ident())
    print(f"pre_save_blog started at: {datetime.datetime.now().strftime('%H:%M:%S')}")
    if not instance.slug:
        instance.slug = slugify(instance.title, allow_unicode=True)
        instance.pub_date = timezone.now()
        print("pre_save_blog")
        print("slug,",instance.slug)
        print("pub_date",instance.pub_date)
    sleep(5)
    print(f"pre_save_blog ended at: {datetime.datetime.now().strftime('%H:%M:%S')}")

@receiver(post_save, sender = Blog)
def post_save_blog(sender,instance , created, **kwargs):
    print("Creating an exception after saving the instance")
    raise Exception("Exception raised after saving the instance")




