from django.db import models


class Business(models.Model):
    name = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255)
    description = models.TextField()
    long_description = models.TextField()

    def __str__(self):
        return self.name


class Page(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    display_in_navbar = models.BooleanField(default=False)
    html_code = models.TextField()

    def __str__(self):
        return self.name


class Card(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    logo_file_path = models.CharField(max_length=255, default=' ')
    html_code = models.TextField()
    page = models.OneToOneField(Page, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Testimony(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=255)
    profile_picture_file = models.CharField(max_length=255)
    testimonial = models.TextField()

    def __str__(self):
        return self.client_name


class Contact(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=128)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name
