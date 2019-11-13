from django.urls import path,include
from . import views
urlpatterns = [
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('gallery',views.gallery,name='gallery'),
    path('service',views.service,name='service'),
    path('accounts/',include('accounts.urls')),
]
