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


class Review(models.Model):
    rating = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField(default=timezone.now)
    body = models.TextField()

    def __str__(self):
        return f"{self.rating}"


class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    body = FroalaField()

    def __str__(self):
        return f"{self.title}"



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




