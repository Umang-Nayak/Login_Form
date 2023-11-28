"""
1) CharField: Used to store short to medium length strings.
-> name = models.CharField(max_length=100)

2) IntegerField: Used to store integer values.
-> age = models.IntegerField()

3) FloatField: Used to store floating-point numbers.
-> price = models.FloatField()

4) DateField and DateTimeField: Used to store dates and date-time values, respectively.
->  birth_date = models.DateField()
    created_at = models.DateTimeField()

5) BooleanField: Used to store boolean (True/False) values.
-> is_active = models.BooleanField(default=True)

6) ForeignKey: Used to define a many-to-one relationship with another model.
->
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

7) ManyToManyField: Used to define a many-to-many relationship with another model.
->
class Tag(models.Model):
    name = models.CharField(max_length=100)

class Article(models.Model):
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)

8) EmailField and URLField: Specialized fields for storing email addresses and URLs, respectively.
->  email = models.EmailField()
    website = models.URLField()

9) ImageField and FileField: Used to store image and file uploads.
->  profile_picture = models.ImageField(upload_to='profile_pics/')
    resume = models.FileField(upload_to='resumes/')

"""


from django.db import models

# Create your models here.


class UserDetails(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_fname = models.CharField(max_length=20)
    u_lname = models.CharField(max_length=20)
    u_contact = models.CharField(max_length=13)
    u_address = models.CharField(max_length=50)
    u_email = models.EmailField(max_length=100)
    u_password = models.CharField(max_length=50)
    is_admin = models.IntegerField(null=True)
    otp = models.CharField(max_length=10, null=True)
    otp_used = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.u_fname} {self.u_lname}"

    class Meta:
        db_table = "UserDetails"
