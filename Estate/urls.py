"""Estate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from products.views import Index,About,Products,Detail,Contact,Search
from users.views import Register,Login,Logout
from accounts.views import Liked,AddLike,Profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Index,name='index'),
    path('about/',About,name='about'),
    path('products/',Products,name='products'),
    path('detail/<int:id>/',Detail,name='detail'),
    path('search/',Search,name='search'),
    path('contact/',Contact,name='contact'),
    path('register/',Register,name='register'),
    path('login/',Login,name='login'),
    path('liked/',Liked,name='liked'),
    path('addlike/<int:id>/',AddLike,name='addlike'),
    path('profile/<int:id>/',Profile,name='profile'),
    path('logout/',Logout,name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
