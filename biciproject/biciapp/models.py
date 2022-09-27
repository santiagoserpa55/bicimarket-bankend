from django.db import models
from datetime import date, timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.hashers import make_password

class UserManager(BaseUserManager):
    def create_user(self, username, password):
        if not username:
            raise ValueError('Debe tener username')
        
        user = self.model(email = username)
        user.set_password(password)
        user.save(using=self._db)
        return user

class Customers(AbstractBaseUser, PermissionsMixin):
    customer_id = models.BigIntegerField(primary_key=True)
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    first_surname = models.CharField(max_length=50)
    second_surname = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, unique=True)
    departament = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    neighborhood = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    password = models.CharField(max_length=150, blank=True)
    #active = models.BooleanField(default=True)

    def save(self, **kwargs):
        some_salt = 'mMUj0DrIK6vgtdIYepkIxN'
        #print(self.password)
        self.password = make_password(self.password, some_salt)
        #print(self.password)
        super().save(**kwargs)

    objects = UserManager()
    USERNAME_FIELD = 'email'

class Bike(models.Model):
    bike_id =  models.AutoField(primary_key=True)
    bike_name = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    bike_category = models.CharField(max_length=25)
    country = models.CharField(max_length=25, blank=True)
    bike_image = models.CharField(max_length=150)
    brand = models.CharField(max_length=25)
    color = models.CharField(max_length=15)
    size_rin = models.CharField(max_length=3, blank=True)
    size_frame = models.CharField(max_length=3, blank=True)
    brake_system = models.CharField(max_length=25)
    year = models.DateField(null=True, blank=True)
    bike_price = models.DecimalField(max_digits=20, decimal_places=2)    
    stock = models.SmallIntegerField(default=1)
    created_at = models.DateField(default=date.today, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    #Order
class Order(models.Model):
    id_order = models.AutoField(primary_key=True)
    id_customer = models.ForeignKey(Customers, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Bike, default=0, on_delete=models.CASCADE)
    cantidad = models.SmallIntegerField(default=1)
    price = models.DecimalField(max_digits=20, decimal_places=3, default=0)
    total = models.DecimalField(max_digits=20, decimal_places=3)
    fecha = models.DateTimeField(auto_now=True)