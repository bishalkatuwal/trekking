from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from datetime import date, datetime
from django.utils.text import slugify
from django.utils import timezone
from ckeditor.fields import RichTextField
from django.urls import reverse





# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    number = models.CharField(blank=True, null=True, max_length=15)
    message = models.TextField()

    def __str__(self):
        return f"{self.name}- {self.number} "
    



class Category(models.Model):
    name = models.CharField(max_length=225, unique=True)
    
    
    def __str__(self):
        return f"{self.name}"
    


class Blog(models.Model):
    title = models.CharField(max_length=225)  
    summary = models.TextField(blank=True, null=True)
    header_image = models.ImageField(blank=True, null=True, upload_to='images/')
    category = models.ForeignKey( Category,  on_delete=models.SET_NULL , blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    body = FroalaField()
    post_date = models.DateTimeField(auto_now_add=True)
   

    def __str__(self):
        return f"{self.title} | {self.author}"


class BlogMedia(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_media')
    image = models.ImageField(upload_to='blog/images', blank=True, null=True)
    vedio = models.FileField(upload_to='blog/video', blank=True, null=True)

    def __str__(self):
        if self.image:
            return f"Image for {self.blog.title}"
        elif self.video:
            return f"Video for {self.blog.title}"
        return f"Media for {self.blog.title}"




class Review(models.Model):
    rating = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField(default=timezone.now)
    body = models.TextField()

    def __str__(self):
        return f"{self.rating}"




class TravelInfo(models.Model):
    title = models.CharField(max_length=100)
    Description = FroalaField()

    def __str__(self):
        return f"{self.title}"




class Destination(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name





class TripCategory(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, null=True)
    image = models.ImageField(upload_to='trip_pics', blank=True, null=True)
    summary = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title




class Trip(models.Model):
    trip_category = models.ForeignKey(
        TripCategory,
        default=1,
        on_delete=models.CASCADE,
        related_name='trips',  # Enables reverse query from TripCategory to Trips
    )
    title = models.CharField(max_length=100)
    cover_img = models.ImageField(upload_to='trips/cover_img', blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    summary = models.TextField(blank=True, null=True)
    description = FroalaField(default="Default description text")
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='trips', default=1)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(default=timezone.now)
    available_seats = models.PositiveBigIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    

    def __str__(self):
        return self.title






class Itinerary(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='itinerary')
    title = models.CharField(max_length=100)  # Title of the day in the itinerary
    day_no = models.PositiveIntegerField()  # Day number in the trek
    distance = models.DecimalField(max_digits=5, decimal_places=2, help_text="Distance in kilometers")  # Distance of the day's trek
    trek_duration = models.DecimalField(max_digits=5, decimal_places=2, help_text="Duration in hours")  # Duration of the trek in hours
    highest_altitude = models.DecimalField(max_digits=7, decimal_places=2, help_text="Maximum altitude in meters")  # Max altitude for the day
    flight_hours = models.DecimalField(max_digits=5, decimal_places=2, help_text="Flight hours if applicable", blank=True, null=True)  # Flight hours (if applicable)
    summary = FroalaField()  # Rich text field for detailed description

    class Meta:
        ordering = ['day_no']  # Ordering by day_no

    def __str__(self):
        return f"Day {self.day_no}: {self.title} - {self.trip.title}"


class TripMedia(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name='media')
    image = models.ImageField(upload_to='trip_images/', null=True, blank=True)
    video = models.FileField(upload_to='trips_videos/', null=True, blank=True)
    caption = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        if self.image:
            return f"Image for {self.trip.title}"
        elif self.video:
            return f"Video for {self.trip.title}"
        return f"Media for {self.trip.title}"



class Page(models.Model):
    STATUS_CHOICES = [
        ('private', 'Private'),    # Only visible to logged-in users or admins
        ('public', 'Public'),      # Visible to all users
    ]
    title= models.CharField(max_length=100)
    parent = models.ForeignKey(
        'self',  # Refers to the same model
        null=True,
        blank=True,
        related_name='children',  # Creates a reverse relation
        on_delete=models.CASCADE
    )
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    sub_title = models.CharField(max_length=200, blank=True, null=True)
    summary = RichTextField(blank=True, null=True)
    description = RichTextField(blank=True, null=True)
    meta_title = models.CharField(max_length=200, blank=True, null=True)
    meta_keyword = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='pages/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='private')

    def save(self, *args, **kwargs):
        if not self.slug: 
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('page_detail', args=[self.slug])


    def __str__(self):
        return self.title




class ChildPage(models.Model):
    parent = models.ForeignKey('Page', related_name='child_pages', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    status = models.CharField(max_length=10, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft')
    created_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    


class TripBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    add_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'trip')
    
    def __str__(self):
        return f"{self.user.username}'s list - {self.trip.title}"



class Language(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):

        return self.name 


class Guide(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='guide/photo', null=True, blank=True)
    bio = models.TextField(blank=True, null= True)
    experience_years = models.PositiveIntegerField(default=1)
    language_spoken = models.ManyToManyField(Language, related_name='language')

    available_from = models.DateField(default=timezone.now)
    available_to = models.DateField(default = timezone.now)
    daily_rate = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    hourly_rate = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    date_joined = models.DateField(default = timezone.now)

    # social media link

    facebook = models.URLField(max_length=255, blank=True, null=True)
    twitter = models.URLField(max_length=255, blank=True, null=True)
    instagram = models.URLField(max_length=255, blank=True, null=True)
    linkedin = models.URLField(max_length=255, blank=True, null=True)
    whatsapp = models.URLField(max_length=255, blank=True, null=True)



    def __str__(self):
        return f"Guide: {self.name}" 



class Materials(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='materials/image')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    quantity = models.PositiveIntegerField(default=0)  # To keep track of stock

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materials"

    def update_stock(self, quantity):
        """
        Custom method to update the stock quantity for an item.
        """
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
        self.quantity = quantity
        self.save()

    def is_in_stock(self):
        """
        Check if the item is in stock to determine if it can be added to the cart.
        """
        return self.quantity > 0

    def decrease_stock(self, quantity):
        """
        Decreases the stock by the given quantity when an item is added to the cart or sold.
        """
        if self.quantity >= quantity:
            self.quantity -= quantity
            self.save()
        else:
            raise ValueError("Not enough stock available.")





class AddToCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    materials = models.ForeignKey(Materials, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  # Add this line to track the quantity
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s cart - {self.materials.title} (x{self.quantity})"





class Booking(models.Model):
    trips = models.ForeignKey(Trip, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    contact = models.CharField(max_length=15)
    emergency_contacts = models.TextField()
    booking_date = models.DateTimeField(auto_now_add=True)
    participants = models.PositiveBigIntegerField()
    country = models.CharField(max_length=100)
    arrival_date = models.DateField()
    departure_date = models.DateField()
    others_information = models.TextField()


    def __str__(self):
        return f"{self.full_name} - {self.email}"
    




