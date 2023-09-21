from django.db import models
from django.contrib.auth.models import User,AbstractUser,Group, Permission
from django.contrib.auth.forms import UserCreationForm
from django import forms
# Create your models here.
class category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class sub_category(models.Model):

    sub_category_id = models.AutoField(primary_key=True)
    sub_name = models.CharField(max_length=100)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    def __str__(self):
        return self.sub_name
    
class brands(models.Model):
    brand_id =  models.AutoField(primary_key=True)
    name= models.CharField(max_length=150)
    def __str__(self):
        return self.name
    
class products(models.Model):
    availablility = (('In Stock','In Stock'),('Out of Stock','Out of Stock'))
    product_id = models.AutoField(primary_key=True)
    image = models.ImageField(upload_to='ultrashop/pimg')
    image2 = models.ImageField(upload_to='ultrashop/pimg',null=True)
    image3 = models.ImageField(upload_to='ultrashop/pimg',null=True)
    name= models.CharField(max_length=150)
    price = models.IntegerField()
    quantity = models.IntegerField(null=True)
    date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE, null = False, default = '')
    sub_category = models.ForeignKey(sub_category, on_delete=models.CASCADE, null = False, default = '')
    brand =models.ForeignKey(brands, on_delete=models.CASCADE, null= True)
    details = models.TextField(max_length=1000,null=True)
    

 
    availablility = models.CharField(choices=availablility,null=True, max_length=45)
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_products_by_id(ids):
        return products.objects.filter(id__in = ids)
    

class CustomUser(AbstractUser):
    billing_address = models.CharField(max_length=255, blank=True, null=True)
    billing_address2 =models.CharField(max_length=255, blank=True, null=True)
    phoneno = models.CharField(max_length=15, blank=True, null=True)
    credit_card_no = models.CharField(max_length=25, blank=True, null=True)

    groups = models.ManyToManyField(Group, blank=True, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='customuser_set')

class UserCreateForm(UserCreationForm):
     email = forms.EmailField(
        required=True,
        label='Email',
        error_messages={'email': 'Email already exists!'}
    )

     class Meta:
        model = CustomUser  # Use the custom user model
        fields = (
            'username',  'first_name', 'last_name','email','billing_address',
            'billing_address2','credit_card_no', 'phoneno',
             'password1', 'password2',  # Include the custom fields here
        )
 

     def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        placeholders = {
            'username': 'Enter Username',
            'first_name': 'Enter First Name',
            'last_name': 'Enter Last Name',
            'email': 'Enter Email Address',
            'billing_address':'Enter Billing Address',
            'billing_address2':'Enter Second Billing Address(Optional)',
            'credit_card_no':'Enter Credit Crard Number (Optional)',
            'phoneno' : 'Enter Contact Number',
            'password1': 'Enter Password',
            'password2': 'Confirm Password',
         
            
        }

        for field_name in placeholders:
            self.fields[field_name].widget.attrs['placeholder'] = placeholders[field_name]

     def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
        return user

     def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email already exists')
        return email
  
# class wishlist_item(models.Model):
#     user= models.ForeignKey(User, on_delete=models.CASCADE)
#     wishlist_item_id = models.AutoField(primary_key=True)
#     product = models.ForeignKey(products, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.product
# class wishlist(models.Model):
#     wishlist_n = models.BooleanField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(products, on_delete=models.CASCADE)