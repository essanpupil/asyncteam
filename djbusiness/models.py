from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    tagline = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Page(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(null=True, blank=True)
    display_in_navbar = models.BooleanField(default=False)
    html_code = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Card(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    logo_file_path = models.CharField(max_length=255, null=True, blank=True)
    html_code = models.TextField(null=True, blank=True)
    page = models.OneToOneField(Page, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Testimony(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=255)
    profile_picture_file = models.CharField(max_length=255, null=True, blank=True)
    testimonial = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.client_name


class Contact(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, )
    phone = models.CharField(max_length=128, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
