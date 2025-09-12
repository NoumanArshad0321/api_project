from django.http import Http404, JsonResponse
from django.shortcuts import render
from blogs.models import Blog, Comment
from blogs.serializers import BlogSerializer, CommentSerializer
from employees.models import Employee
from students.models import Student
from.serializers import EmployeeSerializer, StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework import viewsets

# Create your views here.
@api_view(['GET', 'POST'])
def studentsView(request):
    if request.method=="GET":
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method=="POST":
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def studentsDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        
    if request.method=="GET":
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method=="PUT":
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
    
# *************** CLASS BASED VIEWS *******************

"""class employeesView(APIView):
    def get(self, request):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def post(self,request):
        serializer=EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class employeesDetail(APIView):
    def get_object(self, pk):
        try:
            employee = Employee.objects.get(pk=pk)
            return employee
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk):

        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    

    # def post(self, request, pk):
    #     serializer = EmployeeSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_200_OK)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk):
        employee = self.get_object(pk)
        employee.delete()
       return Response(status=status.HTTP_204_NO_CONTENT)
"""


# ************* MIXINS  AND GENERICS **************

"""class employeesView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)
    

class employeesDetail(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin , mixins.DestroyModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get (self, request,pk):
        return self.retrieve(request, pk)
    
    def put(self, request, pk):
        return self.update(request, pk)
    
    def delete(self, request, pk):
        return self.destroy(request, pk)"""
    

    # ******************** End of MIXINS AND GENERICS ********************


# *************** GENERICS OVER *****************


"""class employeesView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class employeesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer"""





# *************** VIEWSETS ***********************


class employeesViewSet(viewsets.ViewSet):
    def list(self, reuquest):
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    def create(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

    def retrieve(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def update(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk):
        try:
            employee = Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    



 # *************************** MODEL VIEW SETS ***********************  # 

# class employeesViewSet(viewsets.ModelViewSet):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer




class BlogView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer




class CommentView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
