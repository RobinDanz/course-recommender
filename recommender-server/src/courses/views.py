from courses.models import Course
from courses.serializers import CourseSerializer
from rest_framework import generics


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.prefetch_related('tracks').all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.prefetch_related('tracks').all()
    serializer_class = CourseSerializer
