from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from fuzzy.serializers import FormSerializer, TeacherFormSerializer, StudentFeedbackSerializer
from fuzzy.logic import fuzzy_controller
from courses.models import Course

class FormView(APIView):
    def get_serializer(self, *args, **kwargs):
        return FormSerializer(*args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid():
            FS = fuzzy_controller.FuzzyController()
            result = FS.inference(serializer.data)
            print(result)
            return Response(result, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TeacherFormView(APIView):
    def get_serializer(self, *args, **kwargs):
        return FormSerializer(*args, **kwargs)
    
    def post(self, request, id, *args, **kwargs):
        serializer = TeacherFormSerializer(data=request.data)
        if serializer.is_valid():
            Course.objects.filter(pk=id).update(
                subject_type=serializer.data['subject_type'],
                interactions=serializer.data['interactions'],
                blackboard=serializer.data['blackboard'],
                recordings=serializer.data['recordings'],
                teacher_accessibility=serializer.data['teacher_accessibility'],
                teacher_form_filled=True
            )
            FS = fuzzy_controller.FuzzyController().create_fuzzy()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StudentFormView(APIView):
    def get_serializer(self, *args, **kwargs):
        return StudentFeedbackSerializer(*args, **kwargs)

    def post(self, request, id, *args, **kwargs):
        serializer = StudentFeedbackSerializer(data=request.data)
        if serializer.is_valid():
            course = Course.objects.get(pk=id)
            course.update_student_feeback(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
        
