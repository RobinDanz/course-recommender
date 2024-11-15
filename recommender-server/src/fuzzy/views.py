from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from fuzzy.serializers import FormSerializer, TeacherFormSerializer
from fuzzy.logic import fuzzy_controller



class FormView(APIView):
    def get_serializer(self, *args, **kwargs):
        return FormSerializer(*args, **kwargs)
    def post(self, request, *args, **kwargs):
        serializer = FormSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            FS = fuzzy_controller.create_fuzzy()
            result = fuzzy_controller.fuzzy_set_variables(serializer.data, FS)
            print(result)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TeacherFormView(APIView):
    def get_serializer(self, *args, **kwargs):
        return FormSerializer(*args, **kwargs)
    
    def post(self, request, id, *args, **kwargs):
        serializer = TeacherFormSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentFormView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TeacherFormSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
        
