from django.shortcuts import render
from .serializer import ProfileSerializer, ServiceSerializer
from servicesApp.models import Profile, Service
from .permissions import IsAdminOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from django.http import Http404, HttpResponse
from rest_auth.registration.views import SocialLoginView



# API

# profile
class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        profiles = Profile.objects.all()
        serializers = ProfileSerializer(profiles, many=True)
        return Response(serializers.data)


    def post(self, request, format=None):
        serializers = Profile(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleProfile(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_project(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.get_project(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)

    
    def put(self, request, pk, format=None):
        profile= self.get_project(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_project(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# service
class ServiceList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self, request, format=None):
        services = Service.objects.all()
        serializers = ServiceSerializer(services, many=True)
        return Response(serializers.data)


    def post(self, request, format=None):
        serializers = Service(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)





class SingleService(APIView):
    permission_classes = (IsAuthenticated,)
    def get_project(self, pk):
        try:
            return Service.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        service = self.get_project(pk)
        serializers = ServiceSerializer(service)
        return Response(serializers.data)

    
    def put(self, request, pk, format=None):
        service= self.get_project(pk)
        serializers = ProfileSerializer(service, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        service = self.get_project(pk)
        service.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




# socialAuth
# class GoogleLogin(SocialLoginView):
#     adapter_class = GoogleOAuth2Adapter
#     def post(self, request, *args, **kwargs):
        
#             response = super(GoogleLogin, self).post(request, *args, **kwargs)
#             token = Token.objects.get(key=response.data['key'])
#             return Response({'token': token.key, 'id': token.user_id})


