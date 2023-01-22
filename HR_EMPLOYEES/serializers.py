from rest_framework import serializers
from .models import *


class SomEmpDataSerializer(serializers.ModelSerializer):

    JobTitles = serializers.StringRelatedField()

    class Meta:
        model = User
        fields = ['id' , 'first_name','last_name','JobTitles','ProfileImg']

class allEmpDataSerializer(serializers.ModelSerializer):
    
    JobTitles = serializers.StringRelatedField()
    branch = serializers.StringRelatedField()
    direct_manager = serializers.StringRelatedField()


    class Meta:
        model = User
        fields = ['id' , 'first_name','last_name','JobTitles','ProfileImg' ,
                  'CV' , 'father_name' , 'mother_name' , 'emergancy_contact' ,
                  'salary' , 'branch' , 'direct_manager']


class available_departmentSerializer(serializers.ModelSerializer):
    
    management = serializers.StringRelatedField()

    class Meta:
        model = Department
        fields = "__all__"



class JobTitle_createSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = JobTitle
        fields = '__all__'

class Department_createSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'



