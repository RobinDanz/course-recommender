from rest_framework import serializers
from courses.models import Course, Track, Comment
from fuzzy.logic import fuzzy_controller

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        FS = fuzzy_controller.FuzzyController()

        data['lectures_tooltip'] = FS.get_linguistic_var('lectures', data['lectures'])
        data['subject_type_tooltip'] = FS.get_linguistic_var('subject_type', data['subject_type'])
        data['interactions_tooltip'] = FS.get_linguistic_var('interactions', data['interactions'])
        data['blackboard_tooltip'] = FS.get_linguistic_var('blackboard', data['blackboard'])
        data['recordings_tooltip'] = FS.get_linguistic_var('recordings', data['recordings'])
        data['teacher_accessibility_tooltip'] = FS.get_linguistic_var('teacher_accessibility', data['teacher_accessibility'])

        if data['feedback_count'] != 0:
            data['lectures_fb'] = data['lectures_fb'] / data['feedback_count']
            data['subject_type_fb'] = data['subject_type_fb'] / data['feedback_count']
            data['interactions_fb'] = data['interactions_fb'] / data['feedback_count']
            data['blackboard_fb'] = data['blackboard_fb'] / data['feedback_count']
            data['recordings_fb'] = data['recordings_fb'] / data['feedback_count']
            data['teacher_accessibility_fb'] = data['teacher_accessibility_fb'] / data['feedback_count']

            data['lectures_fb_tooltip'] = FS.get_linguistic_var('lectures', data['lectures_fb'])
            data['subject_type_fb_tooltip'] = FS.get_linguistic_var('subject_type', data['subject_type_fb'])
            data['interactions_fb_tooltip'] = FS.get_linguistic_var('interactions', data['interactions_fb'])
            data['blackboard_fb_tooltip'] = FS.get_linguistic_var('blackboard', data['blackboard_fb'])
            data['recordings_fb_tooltip'] = FS.get_linguistic_var('recordings', data['recordings_fb'])
            data['teacher_accessibility_fb_tooltip'] = FS.get_linguistic_var('teacher_accessibility', data['teacher_accessibility_fb'])

        return data

    class Meta:
        model = Course
        fields = '__all__'