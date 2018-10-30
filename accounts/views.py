from django.shortcuts import render,get_object_or_404,redirect
from .models import Like
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from products.models import Product
from django.contrib import messages
from django.contrib.auth.models import User
from realtors.models import Realtor
from django.contrib.auth.decorators import login_required

@login_required(login_url= 'login')
def Liked(request):

  products = Like.objects.filter(user= request.user).order_by('-date')

  paginator = Paginator(products, 6)
  page = request.GET.get('page')
  paged_products = paginator.get_page(page)

  context = {
    'products': paged_products
  }

  return render(request,'liked.html',context)


@login_required(login_url= 'login')
def AddLike(request,id):

  product = Like.objects.filter(product_id= id)

  if product:
    product.delete()
    messages.info(request,'Ürün başarıyla silindi')
  else:
    like = Like(user= request.user, product_id= id)
    like.save()
    messages.success(request,"Ürün beğenilenler'e eklendi")
      
  return redirect('index')


def Profile(request,id):

  info = get_object_or_404(User,id=id)

  realtor = get_object_or_404(Realtor,user_id= id)

  products = Product.objects.filter(realtor_id=id)

  length = len(products)

  paginator = Paginator(products, 6)
  page = request.GET.get('page')
  paged_products = paginator.get_page(page)

  context= {
    'info':info,
    'products':paged_products,
    'realtor':realtor,
    'len':length
  }

  return render(request,'profile.html',context)
