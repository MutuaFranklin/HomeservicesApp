from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.
class Service(models.Model):
    service_image = CloudinaryField('Service Image', blank=True)
    service_title = models.CharField(max_length=20, blank=True, unique=True)
    description= models.TextField(blank=True)


    def __str__(self):
        return self.service_title

    def save_service(self):
        self.save()

    def delete_service(self):
        self.delete() 

    @classmethod
    def search_service(cls, service_title):
        return cls.objects.filter(service_title__icontains=service_title).all()


class Profile(models.Model):
    gender_choice = ("Male", "Male"),("Female","Female")
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    profile_pic = CloudinaryField('Profile Pic', blank=True)
    gender = models.TextField(blank=True, choices=gender_choice)
    mobile = models.CharField(max_length=18, blank=True)
    home_location = models.CharField(max_length = 50,blank=True)
    current_location = models.CharField(max_length = 50,blank=True)
    bio =  models.TextField(blank=True, default='Readily available')
    main_service = models.ForeignKey(Service, on_delete=models.CASCADE ,related_name= 'main_service',blank=True, null=True)
    secondary_service_one = models.ForeignKey(Service, on_delete=models.CASCADE ,related_name='service_one', blank=True, null=True)
    secondary_service_two = models.ForeignKey(Service, on_delete=models.CASCADE , related_name='service_two', blank=True, null=True)


    def __str__(self):
        return self.user.username

        
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete() 

    @classmethod
    def update_profile(cls, prof_id, updated_bio):
        profile = cls.objects.filter(id = prof_id).update(bio = updated_bio)
        return profile
    
    @classmethod
    def search_profile(cls, username):
        return cls.objects.filter(user__username__icontains=username)



class Review(models.Model):
    rating = ((1, '1'),(2, '2'),(3, '3'),(4, '4'),(5, '5'))
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE ,related_name= 'service',blank=True, null=True)
    task_description= models.TextField(blank=True)
    review = models.TextField()
    rating = models.IntegerField(choices=rating, blank=True)
    reviewed_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    reviewed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.profile} Review'


    def save_review(self):
        self.save()

    def delete_review(self):
            self.delete()

    @classmethod
    def update_review(cls, proj_id, updated_review):
        review = cls.objects.filter(id = proj_id).update(review = updated_review)
        return review


    class Meta:
        ordering = ['-reviewed_on']






