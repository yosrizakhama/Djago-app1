from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30, null = True) 
    last_name = models.CharField(max_length=30, null = True)
    email = models.CharField(max_length=50, null = True)
    date_created = models.DateTimeField(auto_now_add = True)
    age = models.IntegerField(null = True)

    def __str__(self):
        return self.first_name+' '+self.last_name

class Tag(models.Model):
    name = models.CharField(max_length=30, null = True) 
    def __str__(self):
        return self.name

class Book(models.Model):
    CATEGORIES=(
        ('Classic','Classic'),
        ('Comic','Comic'),
        ('Fantasi','Fantasi'),
        ('Herror','Herror')
        )
    name = models.CharField(max_length=30, null = True) 
    author = models.CharField(max_length=30, null = True) 
    price = models.FloatField(null = True)
    categorie = models.CharField(max_length=30, null = True, choices = CATEGORIES) 
    description = models.CharField(max_length=200, null = True) 
    date_created = models.DateTimeField(auto_now_add = True)
    tag = models.ManyToManyField(Tag)
    def __str__(self):
        return self.name+' '+str(self.price)

class Order(models.Model):
    STATUS=(
        ('Pending','Pending'),
        ('Delicered','Delicered'),
        ('Out of order','Out of order'),
        ('In Progress','In Progress')
        )
    date_created = models.DateTimeField(auto_now_add = True)
    status =  models.CharField(max_length=200, null = True, choices = STATUS)
    tag = models.ManyToManyField(Tag)
    costumer = models.ForeignKey(Customer, null = True, on_delete = models.SET_NULL)
    book = models.ForeignKey(Book, null = True, on_delete = models.SET_NULL)
    def __str__(self):
        return 'ORDER  '+str(self.id)