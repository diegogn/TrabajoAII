from django.db import models
from django.contrib.auth.models import User
from atom import Author

# Create your models here.
class IntegerRangeField(models.IntegerField):
    def __init__(self,verbose_name=None,name=None,min_value=None,max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class DecimalRangeField(models.DecimalField):
    def __init__(self,verbose_name=None,name=None,min_value=None,max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.DecimalField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value': self.max_value}
        defaults.update(kwargs)
        return super(DecimalRangeField, self).formfield(**defaults)

class WebUser(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    user = models.OneToOneField(User)
    email = models.EmailField()
    age = IntegerRangeField(min_value=18)
    def __unicode__(self):
        return self.name +" "+ self.surname

    
class Author(models.Model):   
    name = models.CharField(max_length=50)
    
class Editorial(models.Model):   
    name = models.CharField(max_length=50)

class Book(models.Model):
    name = models.CharField(max_length=50)
    ISBN = models.CharField(max_length=17)
    type = models.CharField(max_length=50)
    introduction = models.CharField(max_length=10000)
    sipnosis = models.CharField(max_length=10000)
    author = models.ForeignKey(Author)
    editorial = models.ForeignKey(Editorial)
    def __unicode__(self):
        return self.name +" ("+ self.ISBN +")"
    
class RatingBook(models.Model):
    webUser = models.ForeignKey(WebUser)
    book = models.ForeignKey(Book)
    value = IntegerRangeField(min_value=1,max_value=5)

    