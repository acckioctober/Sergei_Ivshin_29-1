"""
URL configuration for cake_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from pastries import views
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('hello/', views.hello),
    # path('now_date/', views.now_date),
    # path('goodbye/', views.goodbye),
    path('', views.MainPageCBV.as_view()),
    path('pastries/', views.PastriesCBV.as_view(), name='pastries'),
    path('cakes/', views.SpecificCakesCBV.as_view()),
    path('tastes/', views.SpecificTasteCBV.as_view()),
    path('fillings/', views.SpecificFillingCBV.as_view()),
    path('toppings/', views.SpecificToppingCBV.as_view()),
    path('cakes/<int:cake_id>/', views.CakeDetailCBV.as_view()),
    path('create/', views.CakeCreateCBV.as_view()),
    path('event/', views.EventCreateCBV.as_view()),
    path('events/', views.EventListCBV.as_view(), name='events'),
    path('users/register/', user_views.RegisterUserCBV.as_view(), name='register'),
    path('users/login/', user_views.UserLoginCBV.as_view(), name='login'),
    path('users/logout/', user_views.UserLogoutCBV.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
