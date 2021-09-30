from django.urls.conf import include
from . import views
from .views import ProfileList, ServiceList
from django.conf.urls.static import static
from django.urls import path, re_path
# from django.conf import settings




urlpatterns=[

    path('profile/', views.ProfileList.as_view()),
    path('services/', views.ServiceList.as_view()),
    re_path(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',views.SingleProfile.as_view()),
    re_path(r'api/service/service-id/(?P<pk>[0-9]+)/$',views.SingleService.as_view()),



   

]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)



