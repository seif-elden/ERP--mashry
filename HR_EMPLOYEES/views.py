from rest_framework import status , generics
from rest_framework.response import Response

from .serializers import  *
from .models import User , Department , JobTitle
from rest_framework.views import APIView

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
import datetime


# Create your views here.


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class login(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]


    def get(self, request, format=None):
        serializer = SomEmpDataSerializer(request.user)
        
        x = User.objects.filter(direct_manager=request.user)


        if x :
            newdict={'is_direct_manager':1}
            newdict.update(serializer.data)
        else:
            newdict={'is_direct_manager':0}
            newdict.update(serializer.data)
        
        return Response(newdict)


##########################################

class SomEmpData(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]


    def get(self, request, format=None):
        Users = User.objects.all()
        serializer = SomEmpDataSerializer(Users, many=True)
        return Response(serializer.data)

class AddEmp(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = allEmpDatacreat_serializer

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]


class EditEmpData(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = allEmpDataupdate_serializer

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    


class AllEmpData(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = allEmpDataSerializer

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

class DeleteEmpData(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = allEmpDataSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]


    
##########################################
class available_jobs(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        Jobs = JobTitle.objects.all()
        serializer = available_jobsSerializer(Jobs, many=True)
        return Response(serializer.data)

class add_job(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):


        serializer = JobTitle_createSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class delete_job(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk ,format=None):
        try:
            JobTitle.objects.get(pk=pk).delete()
        except:
            return Response(data={'the_title':"couldn't find the_title"},status=status.HTTP_404_NOT_FOUND)

        return Response(data={"succsess":"deleted"})

class edit_job(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]
    def put(self, request, pk, format=None):
        try:
            the_title = JobTitle.objects.get(pk=pk)
        except:
            return Response(data={'job':"couldn't find job with that id"},status=status.HTTP_404_NOT_FOUND)
        
        serializer = JobTitle_createSerializer(the_title, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



##########################################


class available_department(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):

        Departments = Department.objects.all()
        serializer = available_departmentSerializer(Departments, many=True)
        return Response(serializer.data)

class add_department(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):


        serializer = Department_createSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class delete_department(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk ,format=None):
        try:
            Department.objects.get(pk=pk).delete()
        except:
            return Response(data={'the_departmenrt':"couldn't find the_departmenrt"},status=status.HTTP_404_NOT_FOUND)

        return Response(data={"succsess":"deleted"})

class edit_department(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, format=None):
        the_Department = Department.objects.get(pk=pk)
        serializer = Department_createSerializer(the_Department, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


##########################################

class delete_leave_request_user(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk ,format=None):
        try:
            x = leave_request.objects.get(pk=pk)
        except:
            return Response(data={'leave request':"couldn't find the request"},status=status.HTTP_404_NOT_FOUND)
        
        if x.the_leave.user == request.user :
            x.delete()
        else :
            return Response(data={'hackeeeeeeeer':"fuck off"},status=status.HTTP_404_NOT_FOUND)

        return Response(data={"succsess":"deleted"})


   


class add_leave_request(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        the_leave = DaysOff.objects.get(pk=request.data.get("the_leave")) 

        if request.user != the_leave.user :
            return Response(data={"hakeeer":"fuck off"},status=status.HTTP_401_UNAUTHORIZED)
        
        if int(request.data.get("number_of_days_requested")) > the_leave.available_for_this_user :
            return Response(data={"number of days ":"the number you inserted is larger than your limit"},status=status.HTTP_400_BAD_REQUEST)


        serializer = add_leave_requestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



class list_avfruser_leave_request(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        avfruser = DaysOff.objects.filter(user=request.user)
        serializer = DaysOffSerializer(avfruser, many=True)
        return Response(serializer.data)



class list_leave_request_managment(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        if request.user.id == 31 :
            avfrequests = leave_request.objects.filter(accepted_by_direct_manager=True)
        else :
            avfrequests = leave_request.objects.filter(the_leave__user__direct_manager = request.user)

        serializer = list_leave_requestSerializer(avfrequests, many=True)

        return Response(serializer.data)


class list_leave_request_user(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        avfrequests = leave_request.objects.filter(the_leave__user = request.user)

        serializer = list_leave_requestSerializer(avfrequests, many=True)

        return Response(serializer.data)



class response_to_leave_request_managment(generics.UpdateAPIView):
    queryset = leave_request.objects.all()
    serializer_class = edit_leave_requestSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

class response_to_leave_request_hr_managment(generics.UpdateAPIView):
    queryset = leave_request.objects.all()
    serializer_class = edit_leave_request_hr_Serializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]


##########################################

class AddWeakly_leave(generics.CreateAPIView):
    queryset = weakly_leave.objects.all()
    serializer_class = weakly_leaveSerializer

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

class DeleteWeakly_leave(generics.DestroyAPIView):
    queryset = weakly_leave.objects.all()
    serializer_class = weakly_leaveSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]


class List_Weakly_leave(generics.ListAPIView):
    queryset = weakly_leave.objects.all()
    serializer_class = weakly_leaveSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]


##########################################


class Add_yearly_leave(generics.CreateAPIView):
    queryset = yearly_leave.objects.all()
    serializer_class = yearly_leaveSerializer

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

class Delete_yearly_leave(generics.DestroyAPIView):
    queryset = yearly_leave.objects.all()
    serializer_class = yearly_leaveSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]


class List_yearly_leave(generics.ListAPIView):
    queryset = yearly_leave.objects.all()
    serializer_class = yearly_leaveSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

class Edit_yearly_leave(generics.UpdateAPIView):
    queryset = yearly_leave.objects.all()
    serializer_class = yearly_leaveSerializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]


##########################################


class available_leave(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        days_off = DaysOffTypes.objects.all()
        serializer = laeveSerializer(days_off, many=True)
        return Response(serializer.data)

class add_leave(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):


        serializer = laeveSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class delete_leave(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def delete(self, request, pk ,format=None):
        try:
            DaysOffTypes.objects.get(pk=pk).delete()
        except:
            return Response(data={'DaysOffTypes':"couldn't find the leave"},status=status.HTTP_404_NOT_FOUND)

        return Response(data={"succsess":"deleted"})

class edit_leave(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def put(self, request, pk, format=None):
        the_leave = DaysOffTypes.objects.get(pk=pk)
        serializer = laeveSerializer(the_leave, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

##########################################


class user_attendance(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):

        try :
            x = attendance.objects.get(
                user = request.user,
                the_day = datetime.date.today()
                )
            return Response(data={"failed":" تم تسجيل الحضور بالفعل اليوم" } , status=status.HTTP_208_ALREADY_REPORTED)
            
        except :
            attendance.objects.create(
                user = request.user
            )
            return Response(data={"succsess":"تم تسجيل الحضور"} , status=status.HTTP_201_CREATED)


class list_user_attendance_days(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]


    def get(self, request, *args, **kwargs):
        try:
            theuser = User.objects.get(pk=self.kwargs['pk'] )

        except:
            return Response(data={"failed":" لم نتمكن من ايجاد هذا الموظف" } , status=status.HTTP_400_BAD_REQUEST)
            


        attendances = attendance.objects.filter(
            user = theuser
        )
        serializer = attendance_Serializer(attendances, many=True)
        return Response(serializer.data)






##########################################


class available_managements(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):

        days_off = management.objects.all()
        serializer = managementsSerializer(days_off, many=True)
        return Response(serializer.data)


##########################################

class user_equipment(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        equipments = equipment.objects.filter(user=pk)
        
        serializer = user_equipment_erializer(equipments, many=True)

        return Response(serializer.data)

class add_user_to_equipment(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def post(self, request, format=None):

        try :
            theUser = User.objects.get(id=request.data.get("userid"))
        except:
            return Response(data={'userid':"couldn't find User"},status=status.HTTP_404_NOT_FOUND)
        try :
            theequipment = equipment.objects.get(id=request.data.get("equipmentid"))
        except:
            return Response(data={'equipmentid':"couldn't find theequipment"},status=status.HTTP_404_NOT_FOUND)


        theequipment.user.add(theUser)



        return Response(data={"succsess":"added"})

class delete_user_from_equipment(APIView):

    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

    def delete(self, request, format=None):

        try :
            theUser = User.objects.get(id=request.data.get("userid"))
        except:
            return Response(data={'userid':"couldn't find User"},status=status.HTTP_404_NOT_FOUND)
        try :
            theequipment = equipment.objects.get(id=request.data.get("equipmentid"))
        except:
            return Response(data={'equipmentid':"couldn't find theequipment"},status=status.HTTP_404_NOT_FOUND)


        theequipment.user.remove(theUser)



        return Response(data={"succsess":"deleted"})

class delete_equipment(generics.DestroyAPIView):
    queryset = equipment.objects.all()
    serializer_class = user_equipment_erializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]


class edit_equipment(generics.UpdateAPIView):
    queryset = equipment.objects.all()
    serializer_class = user_equipment_erializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]

class AllEquipment(APIView):
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        queryset = equipment.objects.all()
        serializer = equipment_erializer(queryset, many=True)
        return Response(serializer.data)


class AddEquipment(generics.CreateAPIView):
    queryset = equipment.objects.all()
    serializer_class = user_equipment_erializer
    authentication_classes = (CsrfExemptSessionAuthentication, BasicAuthentication)
    permission_classes = [IsAuthenticated]