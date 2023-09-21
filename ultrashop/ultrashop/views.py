from django.shortcuts import render, redirect
from customer.models import category, products, brands
from django.contrib.auth import authenticate,login
from customer.models import UserCreateForm
from django.contrib import messages


def Master(request):
    return render(request,'master.html')

def Index(request):
     cat = category.objects.all() #fetches all cats from dbms
    #  prod = products.objects.all()
     catID = request.GET.get('category') #gets the sub cat ids
     brand = brands.objects.all()
     brandID= request.GET.get('brand')

     if catID:
          product = products.objects.filter(sub_category = catID).order_by('-product_id') #orders by latest posted
    
     elif brandID:
          product = products.objects.filter(brand = brandID).order_by('-product_id')
    
     else: 
          product = products.objects.all()

     context = {
          'category': cat,
          'product' : product,
          'brand':brand,
     }
     return render(request,'index.html', context)

def signup(request):
     if request.method == 'POST': 
          form = UserCreateForm(request.POST)
          if form.is_valid():
               new_user = form.save()
               new_user = authenticate(
                    username = form.cleaned_data['username'],
                    password =  form.cleaned_data['password1']
               )
               #messages.success(request, 'Your account has been created successfully. You can now log in.')
               login(request, new_user)
               return redirect('index')
     else:
          form = UserCreateForm()
     context = {
          'form': form,
     }
     return render(request,'registration/signup.html',context)

#prod page
def product(request):
     cat = category.objects.all() 
     brand = brands.objects.all()
     catID = request.GET.get('category') #gets the sub cat ids
     brandID= request.GET.get('brand')

     if catID:
          product = products.objects.filter(sub_category = catID).order_by('-product_id') #orders by latest posted
    
     elif brandID:
          product = products.objects.filter(brand = brandID).order_by('-product_id')
    
     else: 
          product = products.objects.all()

     context = {
          'category': cat,
          'brand': brand,
          'product' : product,
     }
     return render(request,'product.html',context)

#prod details

def product_detail(request,id):
     product = products.objects.filter(product_id= id).first()
     p = products.objects.all()
     brand = brands.objects.all()
     cat = category.objects.all() 
     context={
          'product': product,
          'p': p,
          'brand': brand,
          'category': cat,
     }
     return render(request,'product_detail.html',context)

# def wishlist_add(request):
#      product = products.objects.filter(product_id= id).first()
#      p = products.objects.all()
#      brand = brands.objects.all()
#      cat = category.objects.all() 
#      context={
#           'product': product,
#           'p': p,
#           'brand': brand,
#           'category': cat,
#      }
#      return render(request,'wishlist.html',context)

# def add_to_wishlist(request, product_id):
#     product = products.objects.get(pk=product_id)
#     user = request.user

#     # Check if the product is already in the user's wishlist
#     if wishlist.objects.filter(user=user, product=product).exists():
#         # Product is already in the wishlist, handle this as you wish (e.g., show a message)
#          messages.warning(request, 'This product is already in your wishlist.')
#     else:
#         # Add the product to the user's wishlist
#         wishlist.objects.create(user=user, product=product)

#     return redirect('product_details', product_id=product_id)  # Redirect to the product details page

# def wishlist_v(request):
#     user = request.user
#     wishlist_items = wishlist.objects.filter(user=user)

#     return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})