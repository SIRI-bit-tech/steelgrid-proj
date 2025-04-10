from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField

class Service(models.Model):
    title = models.CharField(max_length=200)
    icon = models.CharField(max_length=50, help_text="Font Awesome icon class")
    short_description = models.CharField(max_length=200)
    description = RichTextField()
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/')
    description = RichTextField()
    completion_date = models.DateField()
    client = models.CharField(max_length=200)
    
    class Meta:
        ordering = ['-completion_date']
    
    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    bio = RichTextField()
    image = models.ImageField(upload_to='team/')
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = RichTextField()
    image = models.ImageField(upload_to='blog/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog_detail', args=[self.slug])

class ContactMessage(models.Model):
    STATUS_CHOICES = [
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]
    
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    company = models.CharField(max_length=200, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    def get_absolute_url(self):
        return reverse('admin:core_contactmessage_change', args=[self.pk])
