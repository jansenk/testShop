from django.db import models
from localflavor.us.models import USStateField, USZipCodeField
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length="12")

class Product(models.Model):
    name = models.CharField(max_length="64")
    description = models.CharField(max_length="120")
    pricePerUnit = models.DecimalField()
    active = models.BooleanField(default=True)
    available = models.IntegerField()
    category = models.ForeignKey(Category)
    provider = models.ForeignKey(Provider)

class Provider(models.Model):
    name = models.CharField
    mailingAddress = models.OneToOneField(Address)
    billingAddress = models.OneToOneField(Address)

class Address(models.Model):
    name = models.CharField(max_length="120")
    address_line_one = models.CharField(max_length="160")
    address_line_two = models.CharField(max_length="160")
    city = models.CharField(max_length="160")
    state = USStateField()
    zip = USZipCodeField()

    def __str__(self):
        # name \n line 1  \n line 2 \n city, state zip
        return "%s\n%s\n%s\n%s, %s %s" % (self.name, self.address_line_one, self.address_line_two, self.city, \
                                          self.state, self.zip)

class UserDetails(models.Model):
    user = models.OneToOneField(User)
    cart = models.CommaSeparatedIntegerField(max_length=20)



