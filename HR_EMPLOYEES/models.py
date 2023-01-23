from django.db import models
from django.contrib.auth.models import AbstractUser


from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.



class management(models.Model):
    management = models.CharField(max_length=255)

    def __str__(self):
        return self.management
    

class Department(models.Model):
    Department = models.CharField(max_length=255)
    management = models.ForeignKey(management,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.Department
    
class JobTitle(models.Model):
    JobTitle = models.CharField(max_length=255)
    Department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return self.JobTitle

    
class branches(models.Model):
    branche = models.CharField(max_length=255)

    def __str__(self):
        return self.branche

    
class User(AbstractUser):


    JobTitle = models.ForeignKey(JobTitle ,on_delete=models.CASCADE,null=True , related_name='JobTitles')
    ProfileImg = models.ImageField(upload_to ='images/uploads/')
    CV = models.FileField(upload_to ='images/uploads/')

    father_name = models.CharField(max_length=255)
    mother_name = models.CharField(max_length=255)
    emergancy_contact = models.IntegerField(null=True)
    salary = models.IntegerField(null=True)
    branch = models.ForeignKey(branches,on_delete=models.CASCADE,null=True)

    direct_manager = models.ForeignKey('self',on_delete=models.CASCADE,null=True)




class DaysOffTypes(models.Model):
    leave_ar = models.CharField(max_length=255)
    leave_en = models.CharField(max_length=255)
    num = models.IntegerField(null=True)

    def __str__(self):
        return self.leave_ar


class DaysOff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    leave_name = models.CharField(max_length=255,null=True)
    available_for_this_user  = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.user} | {self.leave_name} | {self.available_for_this_user}"



@receiver(post_save, sender=User)
def create_DaysOff(sender, instance=None, created=False, **kwargs):
    if created:

        for x in DaysOffTypes.objects.all() :
            DaysOff.objects.create(
                user=instance,
                leave_name=x.leave_ar,
                available_for_this_user = x.num

                
            
            )
    
