from rest_framework import serializers

class FormSerializer(serializers.Serializer):
    evaluation = serializers.ListField()
    university = serializers.ListField()
    course_type = serializers.ListField()
    track = serializers.ListField()
    lectures = serializers.ListField()
    subject_type = serializers.IntegerField()
    interactions = serializers.IntegerField()
    blackboard = serializers.IntegerField()
    recordings = serializers.IntegerField()
    teacher_accessibility = serializers.IntegerField()