from django.db import models

# Create your models here.
class Leader(models.Model):
    GENDER_CHOICES = (
        ("female", "Female"),
        ("male", "Male"),
    )
    TRACK_CHOICES = (
        ("design", "Design"),
        ("frontend", "Frontend"),
        ("backend", "Backend"),
    )
    LANGUAGE_CHOICES = (
        ("python", "Python"),
        ("javascript", "Javascript"),
        ("java", "Java"),
        ("Go", "Go"),
        ("Php", "Php"),
    )
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, default="female"
    )

    track = models.CharField(
        max_length=10, choices=TRACK_CHOICES, default="backend"
    )
    language = models.CharField(
        max_length=10, choices=LANGUAGE_CHOICES, default="python"
    )
    points = models.DecimalField(max_digits = 5, decimal_places = 2)

    def __str__(self):
        return self.first_name


    
class Members(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    gender = models.CharField( max_length=10)
    track = models.CharField( max_length=10 )
    language = models.CharField( max_length=10)
    points = models.DecimalField(max_digits = 5, decimal_places = 2)

    def __str__(self):
        return self.first_name





