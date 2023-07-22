from django.db import models

# Create your models here.
#product models
class Product(models.Model):
    name = models.CharField(max_length=10)
    email= models.EmailField(default="")
    def __str__(self):
        return self.name
 # signup models.
class Signup(models.Model):
    Name = models.CharField(max_length=10)
    Email = models.EmailField()
    Mobile_No = models.IntegerField()
    Password = models.CharField(max_length=8)
    def __str__(self):
        return self.Name
#Blog project
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
            return self.name

class Author(models.Model):
        name = models.CharField(max_length=200)
        email = models.EmailField()

        def __str__(self):
            return self.name

class Entry(models.Model):
        blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
        headline = models.CharField(max_length=255)
        body_text = models.TextField()
        pub_date = models.DateField()
        mod_date = models.DateField()
        authors = models.ManyToManyField(Author)
        number_of_comments = models.IntegerField()
        number_of_pingbacks = models.IntegerField()
        rating = models.IntegerField()

        def __str__(self):
            return self.headline

class Pro(models.Model):
    name = models.CharField(max_length=10)
    des = models.TextField()
    img = models.ImageField(upload_to='pro')
    price = models.IntegerField()
    review = models.TextField()

    def __str__(self):
        return self.name

