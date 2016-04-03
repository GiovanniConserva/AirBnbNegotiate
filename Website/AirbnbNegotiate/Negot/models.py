from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=20)
    reg_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Search(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    search_time = models.DateTimeField(auto_now=True)
    checkin_date = models.DateField()
    chechout_date = models.DateField()
    destination = models.CharField(max_length=254)
    guest_num = models.IntegerField(default=1)
    num_of_results = models.IntegerField(default=0)

    def __str__(self):
        return 'Start: {} - End: {}'.format(self.checkin_date, self.chechout_date)



