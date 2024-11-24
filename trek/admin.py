from django.contrib import admin
from .models import Contact, Blog,ChildPage, TripImage ,Page ,Category,Review, TravelInfo, TripCategory, Trip, Destination
# Register your models here.






admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(TravelInfo)
admin.site.register(Trip)
admin.site.register(TripCategory)
admin.site.register(Destination)
admin.site.register(Page)
admin.site.register(ChildPage)
admin.site.register(TripImage)