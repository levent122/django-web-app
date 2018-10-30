from django.shortcuts import render,get_object_or_404
from .models import Product
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .choices import city_choices,price_choices
from accounts.models import Like


def Index(request):

  products = Product.objects.order_by('-date').filter(is_published=True)[:6]

  context = {
    'products':products,
    'city_choices':city_choices,
    'price_choices':price_choices,
  }

  return render(request,'index.html',context)


def About(request):

    return render(request,'about.html')


def Products(request):

  products = Product.objects.order_by('-date').filter(is_published=True)

  paginator = Paginator(products, 9)
  page = request.GET.get('page')
  paged_products = paginator.get_page(page)

  context = {
    'products': paged_products,
  }

  return render(request, 'products.html', context)


def Detail(request,id):

    product = get_object_or_404(Product, id=id)

    return render(request,'detail.html',{'product':product})


def Contact(request):

  return render(request,'contact.html')


def Search(request):

  products = Product.objects.order_by('-date')

  paginator = Paginator(products, 9)
  page = request.GET.get('page')
  paged_products = paginator.get_page(page)


  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      paged_products = Product.objects.filter(description__icontains=keywords)

  # City
  if 'city' in request.GET:
    city = request.GET['city']
    if city:
      paged_products = Product.objects.filter(city__iexact=city)

  # Price
  if 'price' in request.GET:
    price = request.GET['price']
    if price:
      paged_products = Product.objects.filter(price__lte=price)

  context = {
      'products':paged_products,
      'city_choices':city_choices,
      'price_choices':price_choices,
    }

  return render(request,'search.html',context)