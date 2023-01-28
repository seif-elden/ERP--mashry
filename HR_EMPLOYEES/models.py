from django.db import models
from django.contrib.auth.models import AbstractUser


from django.dispatch import receiver
from django.db.models.signals import post_save 

import datetime



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

    emp_type_options = [
    ('تم التثبيت', 'تم التثبيت'),
    ('يتم التجربة', 'يتم التجربة'),

]
    gender_options = [
    ('مؤنث', 'مؤنث'),
    ('مذكر', 'مذكر'),

]

    ProfileImg = models.ImageField(upload_to ='images/uploads/',null=True)
    CV = models.FileField(upload_to ='images/uploads/',null=True)
    national_id = models.FileField(upload_to ='images/uploads/' , null=True)
    contract_copy = models.FileField(upload_to ='images/uploads/' , null=True)
    insurance = models.FileField(upload_to ='images/uploads/' , null=True)


    gender = models.CharField(
        max_length=20,
        choices=gender_options,
        default= ""
    )

    emp_type = models.CharField(
        max_length=20,
        choices=emp_type_options,
        default= ""
    )

    address = models.CharField(max_length=120 , null=True)

    caontact_number = models.CharField(max_length=12 , null=True)
    bank_account = models.CharField(max_length=255,null=True)
    birthday = models.DateField(null=True)


    emp_id = models.CharField(max_length=255,null=True)

    family_name = models.CharField(max_length=255,null=True)
    emergancy_contact = models.CharField(max_length=12 , null=True)

    
    the_contract_time = models.DateField(null=True)
    salary = models.IntegerField(null=True)
    branch = models.ForeignKey(branches,on_delete=models.CASCADE,null=True)

    direct_manager = models.ForeignKey('self',on_delete=models.CASCADE,null=True)
    JobTitle = models.ForeignKey(JobTitle ,on_delete=models.CASCADE,null=True , related_name='JobTitles')





class DaysOffTypes(models.Model):
    leave_ar = models.CharField(max_length=255)
    num = models.IntegerField(null=True)

    def __str__(self):
        return self.leave_ar


class DaysOff(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    leave_name = models.ForeignKey(DaysOffTypes, on_delete=models.CASCADE, null=True)
    available_for_this_user  = models.IntegerField(null=True)

    def __str__(self):
        return f"{self.user} | {self.leave_name} | {self.available_for_this_user}"



@receiver(post_save, sender=User)
def create_DaysOff_for_new_user(sender, instance=None, created=False, **kwargs):
    if created:

        for x in DaysOffTypes.objects.all() :
            DaysOff.objects.create(
                user=instance,
                leave_name=x,
                available_for_this_user = x.num

                
            
            )

@receiver(post_save, sender=DaysOffTypes)
def create_DaysOff_for_new_leave(sender, instance=None, created=False, **kwargs):
    if created:

        for x in User.objects.all() :
            DaysOff.objects.create(
                user=x,
                leave_name=instance,
                available_for_this_user = instance.num

                
            
            )
    

@receiver(post_save, sender=User)
def create_DaysOff_for_new_user(sender, instance=None, created=False, **kwargs):
    if created:
        year = datetime.date.today().year
        if instance.id < 10 :
            instance.id = f"0{instance.id}"
        instance.emp_id = f"{instance.id}{year}"
        instance.save()


    
