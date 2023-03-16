from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
#User=settings.AUTH_USER_MODEL
# Create your models here.
class productMainModel(models.Model):
    title=models.CharField(max_length=255)
    Description=models.TextField()
    Unique_id=models.CharField(max_length=255,
                               unique=True)
    price=models.IntegerField()


class UserModel(models.Model):

    phone_number=models.CharField(max_length=255,unique=True)
    Email=models.EmailField()
    is_customer= models.BooleanField()
    is_admin=models.BooleanField()



class userProfileModel(models.Model):
    owner=models.OneToOneField(User,on_delete=models.CASCADE)
    Name= models.CharField(max_length=255)
    Date_of_birth= models.CharField(max_length=255)

    choices_Gender= (('1', 'Male'), ('2', 'Female'), ('3', 'Others'))
    Gender=models.CharField(max_length=10, choices=choices_Gender,default=1)
    Image=models.ImageField(upload_to='uploads')

    def __str__(self) -> str:
        return self.Name


class userLoginTopModel(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    Otp=models.IntegerField()
    active=models.BooleanField()




class UserCartProductModel(models.Model):
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(productMainModel,on_delete=models.CASCADE)

    status_choices=((1,'Pending'),
                    (2,'Completed'))
    status=models.CharField(max_length=20,
                            choices=status_choices,
                            default=1)
     
    
class UserCartModel(models.Model):
    owner=models.OneToOneField(User,on_delete=models.CASCADE)
    products=models.ManyToManyField(UserCartProductModel)
    price=models.IntegerField()


class productImageModel(models.Model):
    product=models.ForeignKey(productMainModel,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='uploads')

		


	
