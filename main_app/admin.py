from django.contrib import admin
from .models import Tea, Drinking, Store 

# Register your models here.
admin.site.register(Tea)
admin.site.register(Drinking)
admin.site.register(Store)