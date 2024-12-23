from django.contrib import admin
from .models import( Contact, 
                    Blog,
                    ChildPage,
                    Page ,
                    Category,
                    Review,
                    TravelInfo,
                    TripCategory,
                    Trip,
                    Destination,
                    TripBooking,
                    TripMedia,
                    BlogMedia,
                    Guide,
                    Language,
                    Materials,
                    AddToCart,
                    Itinerary
                    )


class TripMediaInline(admin.TabularInline):
    model = TripMedia
    extra = 1  # This will display one empty form by default

# Custom admin for Trip model to include the media inline
class TripAdmin(admin.ModelAdmin):
    inlines = [TripMediaInline]  # Display TripMedia inline with Trip form

# Register models with custom admin
admin.site.register(Trip, TripAdmin)

class GuideAdmin(admin.ModelAdmin):
    list_display = ('name', 'experience_years', 'daily_rate', 'hourly_rate', 'available_from', 'available_to')
    search_fields = ('name', 'bio')
    list_filter = ('experience_years',)

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)




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
admin.site.register(BlogMedia)
admin.site.register(Guide, GuideAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Materials)
admin.site.register(AddToCart)
admin.site.register(Itinerary)


