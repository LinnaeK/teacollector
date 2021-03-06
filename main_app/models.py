from django.db import models
from django.urls import reverse
from datetime import date 
from django.contrib.auth.models import User 

DRINKS = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

class Store(models.Model):
    name = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    address = models.CharField(default = "", max_length=200)
    city = models.CharField(default = "", max_length = 100)
    phone = models.CharField(max_length=14)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('store_detail', kwargs={'pk': self.id})

class Tea(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    water_temp = models.IntegerField()
    steeping_time = models.IntegerField()
    notes = models.CharField(max_length=200)
    stores = models.ManyToManyField(Store)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'tea_id': self.id})

    def drank_for_today(self):
        return self.drinking_set.filter(date=date.today()).count() >= len(DRINKS)

class Drinking(models.Model):
    date = models.DateField('drinking date')
    time = models.CharField(
        max_length=1, 
        choices=DRINKS,
        default=DRINKS[0][0]
    )
    tea = models.ForeignKey(Tea, on_delete=models.CASCADE)
    feeling = models.CharField(default = "good", max_length=200)

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"

    class Meta:
        ordering = ['-date']

class Meta:
    ordering = ['-date']

class Photo(models.Model):
    url=models.CharField(max_length=200)
    tea=models.ForeignKey(Tea, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Photo for tea_id: {self.tea_id} @ {self.url}"