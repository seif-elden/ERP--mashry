from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view , permission_classes ,authentication_classes
from rest_framework.response import Response

from .serializers import   SomEmpDataSerializer , available_departmentSerializer , JobTitle_createSerializer , Department_createSerializer , allEmpDataSerializer ,available_jobsSerializer
from .models import User , Department , JobTitle


# Create your views here.

@api_view(["GET",])
def SomEmpData(request):

    Users = User.objects.all()
    serializer = SomEmpDataSerializer(Users, many=True)
    return Response(serializer.data)

@api_view(["GET",])
def AllEmpData(request,pk):
    try:
        the_user = User.objects.get(pk=pk)
    except:
        return Response(data={'the_user':"couldn't find the user"},status=status.HTTP_404_NOT_FOUND)

    serializer = allEmpDataSerializer(the_user)
    return Response(serializer.data)



@api_view(["GET",])
def available_department(request):

    Departments = Department.objects.all()
    serializer = available_departmentSerializer(Departments, many=True)
    return Response(serializer.data)

@api_view(["GET",])
def available_jobs(request):

    Jobs = JobTitle.objects.all()
    serializer = available_jobsSerializer(Jobs, many=True)
    return Response(serializer.data)



from rest_framework.views import APIView

from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class add_job(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)


    def post(self, request, format=None):


        serializer = JobTitle_createSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class add_department(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)


    def post(self, request, format=None):


        serializer = Department_createSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
