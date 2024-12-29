from courses.models import Course, Comment
from courses.serializers import CourseSerializer, CommentSerializer
from rest_framework import generics


class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.prefetch_related('tracks').all()
    serializer_class = CourseSerializer


class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.prefetch_related('tracks').all()
    serializer_class = CourseSerializer


class CommentCreate(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
