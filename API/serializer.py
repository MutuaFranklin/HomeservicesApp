from servicesApp.models import Profile, Service
from rest_framework import serializers



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'user','profile_pic', 'gender', 'mobile','home_location', 'current_location' ,'bio','main_service', 'secondary_service_one', 'secondary_service_two' )


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'service_image','service_title', 'description' )


 