from django.contrib import admin
from .models import Contact, Blog,ChildPage ,Page ,Category,Review, TravelInfo, TripCategory, Trip, Destination, TripBooking, TripMedia



class TripMediaInline(admin.TabularInline):
    model = TripMedia
    extra = 1  # This will display one empty form by default

# Custom admin for Trip model to include the media inline
class TripAdmin(admin.ModelAdmin):
    inlines = [TripMediaInline]  # Display TripMedia inline with Trip form

# Register models with custom admin
admin.site.register(Trip, TripAdmin)






admin.site.register(Contact)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Review)
admin.site.register(TravelInfo)
admin.site.register(TripCategory)
admin.site.register(Destination)
admin.site.register(Page)
admin.site.register(ChildPage)
admin.site.register(TripBooking)
admin.site.register(TripMedia)