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
    Department = models.ForeignKey(Department,on_delete=models.CASCADE,null=True , blank=True )
    management = models.ForeignKey(management,on_delete=models.CASCADE,null=True , blank=True)



    def __str__(self):
        return self.JobTitle

    
class branches(models.Model):
    branche = models.CharField(max_length=255)

    def __str__(self):
        return self.branche

    
class User(AbstractUser):

    first_name = models.CharField( max_length=150 )
    last_name = models.CharField( max_length=150)
    email = models.EmailField()

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

    address = models.CharField(max_length=120 , null=True , blank=True)

    caontact_number = models.CharField(max_length=12 , null=True , blank=True)

    bank_account_iban = models.CharField(max_length=255,null=True,blank=True)
    bank_account = models.CharField(max_length=255,null=True,blank=True )
    bank_name = models.CharField(max_length=255,null=True,blank=True)

    paypal_email = models.EmailField(null=True,blank=True)

    birthday = models.DateField(null=True , blank=True)


    emp_id = models.CharField(max_length=255,null=True)

    family_name = models.CharField(max_length=255,null=True ,  blank=True)
    family_relation = models.CharField(max_length=255,null=True, blank=True)
    emergancy_contact = models.CharField(max_length=12 , null=True, blank=True)

    
    the_contract_time = models.DateField(null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)
    branch = models.ForeignKey(branches,on_delete=models.CASCADE,null=True, blank=True)

    direct_manager = models.ForeignKey('self',on_delete=models.CASCADE,null=True, blank=True)
    JobTitle = models.ForeignKey(JobTitle ,on_delete=models.CASCADE,null=True , related_name='JobTitles')
    

    



class equipment(models.Model):

    equipmentName = models.CharField( max_length=50,null=True)
    user = models.ManyToManyField(User)




    def __str__(self):
        return self.equipmentName




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


class weakly_leave(models.Model):

    DAY_OF_THE_WEEK = [
    ('سبت' , 'سبت'),
    ('أحد' , 'أحد'),
    ('اثنين' , 'اثنين'),
    ('ثلثاء' , 'ثلثاء'),
    ('اربعاء' , 'اربعاء'),
    ('خميس' , 'خميس'), 
    ('جمعه' , 'جمعه'),

]

    
    day = models.CharField(max_length=10, choices=DAY_OF_THE_WEEK , unique=True)

    def __str__(self):
        return self.day


class yearly_leave(models.Model):
    name = models.CharField( max_length=50)    
    date = models.DateField(auto_now=False, auto_now_add=False)
    
    def __str__(self):
        return self.name


class leave_request(models.Model):

    the_leave =  models.ForeignKey(DaysOff, on_delete=models.CASCADE , related_name="the_leave")
    number_of_days_requested = models.IntegerField(null=True)
    accepted = models.BooleanField(null=True)
    started_at = models.DateField(auto_now=False, auto_now_add=False,null=True)





    def __str__(self):
        return f"{self.the_leave.user} | {self.the_leave.leave_name} |r {self.number_of_days_requested} | a {self.the_leave.available_for_this_user}"








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


@receiver(post_save, sender=leave_request)
def delete_days_from_avdays(sender, instance=None, created=False, **kwargs):
    
    x = DaysOff.objects.get(pk=instance.the_leave.id)

    if created:

        x.available_for_this_user -= instance.number_of_days_requested
        x.save()

    if instance.accepted == False :
        
        x.available_for_this_user += instance.number_of_days_requested
        x.save()      

    
