from django.contrib import admin
from testjApp.models import productImageModel,productMainModel,userProfileModel,UserCartProductModel,userLoginTopModel,UserCartModel,UserModel
# Register your models here.
admin.site.register(productImageModel)
admin.site.register(productMainModel)
admin.site.register(userProfileModel)
admin.site.register(UserCartProductModel)
admin.site.register(userLoginTopModel)
admin.site.register(UserCartModel)
admin.site.register(UserModel)
