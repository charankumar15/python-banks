from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class AppUser(AbstractUser):
    pass

class BankAccount(models.Model):
    name_in_bank = models.CharField(max_length=20, blank = False, null = False)
    Account_no = models.BigIntegerField(null=False, blank=False)
    ifsc_code = models.CharField(max_length=20, null=False, blank=False)
    Location = models.TextField(null=False, blank=True)

tag_choices = {
    ('popular', 'Popular'),
    ('technology', 'Technology'),
    ('design', 'Design'),
}
class Article(models.Model):
    artice_post_by = models.ForeignKey(AppUser, null=False, blank=False, on_delete=models.CASCADE)
    title = models.CharField(max_length=40, null=False, blank=False)
    body = models.TextField()
    tag = models.CharField(choices=tag_choices,max_length=20)
    posted_on = models.DateTimeField(auto_now=True)