from django.db import models

class Tea(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    water_temp = models.IntegerField()
    steeping_time = models.IntegerField()
    notes = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name