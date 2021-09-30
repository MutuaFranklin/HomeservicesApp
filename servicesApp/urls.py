from django.urls.conf import include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import UpdateProfileView



urlpatterns=[
   
    path('register/', views.register, name='register'),
    path('account/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('about_us/', views.about_us, name='about_us'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('profile/<username>/', views.userProfile, name='profile'),
    path('update-profile/<int:pk>', UpdateProfileView.as_view(), name='update-profile'),
    path('service/<service_title>', views.single_service, name='single_service'),
    path('search/', views.search, name='search_results'),







   


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



