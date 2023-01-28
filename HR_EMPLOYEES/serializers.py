from rest_framework import serializers
from .models import *


class SomEmpDataSerializer(serializers.ModelSerializer):

    JobTitle = serializers.StringRelatedField()


    class Meta:
        model = User
        fields = ['id' ,"date_joined", 'first_name','last_name','JobTitle','ProfileImg' ,'emp_id' ,'email' , 'caontact_number']

class allEmpDataSerializer(serializers.ModelSerializer):

    JobTitle = serializers.StringRelatedField()
    branch = serializers.StringRelatedField()
    direct_manager = serializers.StringRelatedField()


    class Meta:
        model = User
        fields = ['id' , "family_relation",'emp_id' ,'address', 'username', 'first_name' ,'last_name', 'email', 'ProfileImg' , 'CV' , 'national_id' ,
                    "insurance" ,"contract_copy" , 'birthday', 'gender',
                    'caontact_number', 'family_name' , 'emergancy_contact' , 'bank_account' ,
                    'JobTitle' , 'emp_type' , 'salary' ,'the_contract_time', 'branch' , 'direct_manager']


class allEmpDatacreat_updateS_erializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id' , 'family_relation', 'address','password' ,'emp_id' , 'username', 'first_name' ,'last_name','ProfileImg' , 'CV' , 'national_id' ,
                    "insurance" ,"contract_copy" , 'birthday', 'gender',
                    'caontact_number', 'family_name' , 'emergancy_contact' , 'bank_account' ,
                    'JobTitle' , 'emp_type' , 'salary' ,'the_contract_time', 'branch' , 'direct_manager']
        read_only_fields = ('id', 'emp_id')
        extra_kwargs = {
            'password': {'write_only': True}
        }
        

##########################################

class available_departmentSerializer(serializers.ModelSerializer):

    management = serializers.StringRelatedField()

    class Meta:
        model = Department
        fields = "__all__"

class Department_createSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

##########################################

class available_jobsSerializer(serializers.ModelSerializer):

    Department = available_departmentSerializer()

    class Meta:
        model = JobTitle
        fields = '__all__'


class JobTitle_createSerializer(serializers.ModelSerializer):


    class Meta:
        model = JobTitle
        fields = '__all__'


##########################################

class laeveSerializer(serializers.ModelSerializer):

    class Meta:
        model = DaysOffTypes
        fields = '__all__'

##########################################

class managementsSerializer(serializers.ModelSerializer):

    class Meta:
        model = management
        fields = '__all__'

##########################################