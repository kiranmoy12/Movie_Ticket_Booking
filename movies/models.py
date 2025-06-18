from django.db import models

# Create your models here.
genres = [
    ('action', 'Action'),
    ('comedy', 'Comedy'),
    ('drama', 'Drama'),
    ('horror', 'Horror'),
    ('sci-fi', 'Science Fiction'),
    ('romance', 'Romance'),
    ('thriller', 'Thriller'),
    ('animation', 'Animation'),
    ('documentary', 'Documentary'),
    ('fantasy', 'Fantasy'),
    ('mystery', 'Mystery'),
]

languages = [
    ('english', 'English'),
    ('bengali', 'Bengali'),
    ('hindi', 'Hindi'),
    ('odia', 'Odia'),
    ('tamil', 'Tamil'),
    ('telugu', 'Telugu'),
    ('kannada', 'Kannada'),
    ('malayalam', 'Malayalam'),
    ('punjabi', 'Punjabi'),
]

class Movie(models.Model):
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=50,choices=genres,null=True, blank=True)
    language = models.CharField(max_length=50,choices=languages,null=True, blank=True)
    synopsis = models.TextField(null=True, blank=True)
    duration_minuts = models.PositiveIntegerField(null=True, blank=True)  
    release_date = models.DateField(null=True, blank=True)
    trailer_url = models.URLField(null=True, blank=True)
    status = models.CharField(max_length=20, default='available', choices=(('available', 'Available'), ('unavailable', 'Unavailable')))
    created_at = models.DateTimeField(auto_now_add=True)
    movie_image = models.ImageField(upload_to='movies/', null=True, blank=True)

    
    def __str__(self):
        return self.title

class Cast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='casts')
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='casts/', null=True, blank=True)
