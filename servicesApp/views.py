from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile, Review, Service
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReviewForm, UserRegistrationForm, UpdateUserProfileForm
from .email import send_welcome_email
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, request 
from django.conf import settings
import requests
import json



# Create your views here.

MAPBOX_TOKEN = settings.MAPBOX_TOKEN    

# def get_ip_details(ip_address=None):
#         ipinfo_token = getattr(settings, "IPINFO_TOKEN", None)
# 	ipinfo_settings = getattr(settings, "IPINFO_SETTINGS",{})
# 	ip_data = ipinfo.getHandler(ipinfo_token, **ipinfo_settings)
# 	ip_data = ip_data.getDetails(ip_address)
# 	return ip_data

# def location(request): 

# 	ip_data = get_ip_details('168.156.54.5')

# 	response_string = 'The IP address {} is located at the coordinates {}, which is in the city {}.'.format(ip_data.ip,ip_data.loc,ip_data.city)

# 	return HttpResponse(response_string)


def register(request):
    reg_form = UserRegistrationForm()

    if request.method == 'POST':
        reg_form = UserRegistrationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            user = reg_form.cleaned_data.get('username')
            email = reg_form.cleaned_data['email']
            messages.success(request, 'Account was created for ' + user)
            send_welcome_email(user,email)
            return redirect('login')
        else:
            reg_form = UserRegistrationForm()

    
    return render(request, 'registration/sign_up.html', {'reg_form': reg_form})


def login_user(request):
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'registration/login.html')


def home(request):
    services = Service.objects.all()[:4]

    context = {
        "services":services
       
    }
    return render(request, 'homeservices/index.html', context)

def about_us(request):
    
       
    context = {
       
    }
    return render(request, 'homeservices/about.html', context)


def services(request):
    services = Service.objects.all()
    
       
    context = {
        "services":services
       
    }
    return render(request, 'homeservices/services.html', context)

@login_required(login_url='login')
def single_service(request, service_title):
    service = Service.objects.filter(service_title=service_title)

    for profile in service:
            main = Profile.objects.filter(main_service = profile.id)
            secondary_one = Profile.objects.filter(secondary_service_one = profile.id)
            secondary_two = Profile.objects.filter(secondary_service_two = profile.id)
            print(secondary_one)



   

       
    context = {
        "service":service,
        "main":main,
        "secondary_one":secondary_one,
        'secondary_two':secondary_two,
       
    }
    return render(request, 'homeservices/single_service.html', context)



def portfolio(request):
     
    
    mapbox_access_token = MAPBOX_TOKEN

    # mapbox_access_token = 'pk.my_mapbox_access_token'

    print(mapbox_access_token)
                  
       
    context = {

     'mapbox_access_token': mapbox_access_token ,
       
    }
    return render(request, 'homeservices/portfolio.html', context)

ip ='154.122.77.79'
def userProfile(request, username):
    current_user = request.user
    user = get_object_or_404(User, username=username)
    userProfile = Profile.objects.get(user=user)
    reviews = Review.objects.filter(profile=userProfile)



    #Review Form
    if request.method == 'POST':
        reviewForm = ReviewForm(request.POST, request.FILES)
        if reviewForm.is_valid():
            profile_review = reviewForm.save(commit=False)
            profile_review.profile = userProfile
            profile_review.reviewed_by = current_user
            profile_review.save()
            return redirect(request.META.get('HTTP_REFERER'))
    else:
        reviewForm = ReviewForm()
   

    # x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    # if x_forwarded_for:
    #     ip = x_forwarded_for.split(',')[0]
    # else:
    #     ip = request.META.get('REMOTE_ADDR')
    res = requests.get('http://ip-api.com/json/'+ ip)
    location_data_one = res.text
    location_data = json.loads(location_data_one)
    # print(location_data)    
    context = {
        "profile":userProfile,
        "geodata":location_data,
        "reviewForm":reviewForm,
        "reviews":reviews,

       
    }
    return render(request, 'profile/userProfile.html', context)


class UpdateProfileView(UpdateView):
        model=Profile
        slug_field = "username"
        form_class =UpdateUserProfileForm
        template_name ='profile/editProfile.html'
        
        def get_queryset(self): 
            return Profile.objects.all()


        def get_success_url(self):
        
            return reverse_lazy('profile',args=[self.request.user.username]) 


def search(request):
    current_user = request.user
    profile = Profile.objects.filter(current_location=current_user.profile.current_location).all()

    if 'search_query' in request.GET and request.GET["search_query"]:
        # form data
        search_service = request.GET.get("search_query")
        search_profile = request.GET.get("search_query")
        # print(search_service)

        # search results
        searched_service =Service.search_service(search_service)
        searched_profile =Profile.search_profile(search_profile)


        # print(searched_business)
        service_message = f"{search_service}"
        profile_message = f"{search_profile}"


        context = {
            "s_message":service_message,
            "p_message":profile_message,
            "services": searched_service,
            "profiles": searched_profile,
            "service_provider":profile
        }


        return render(request, 'homeservices/search.html', context)

    else:
        message = "You haven't searched for any term"
        return render(request, 'homeservices/search.html',{"message":message})


