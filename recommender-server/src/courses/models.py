from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=255)
    day = models.PositiveSmallIntegerField()
    type = models.PositiveSmallIntegerField()
    site = models.PositiveSmallIntegerField()
    code = models.CharField(max_length=50)
    start = models.TimeField(null=True)
    end = models.TimeField(null=True)
    semester = models.PositiveSmallIntegerField()
    description = models.TextField()
    url = models.URLField()
    teacher_form_filled = models.BooleanField(default=False)
    tracks = models.ManyToManyField(to='courses.Track')
    feedback_count = models.IntegerField(default=0)

    #Fuzzy parameters
    evaluation = models.FloatField(default=0) #how is the course evaluated
    university = models.FloatField(default=0) #what university
    course_type = models.FloatField(default=0) #seminar or course 
    lectures = models.FloatField(default=0) #is the course only lecture or only project or in between
    subject_type = models.FloatField(default=0) #theoritical or practical
    interactions = models.FloatField(default=0) #interactions between student and teacher
    blackboard = models.FloatField(default=0) #how much the blackboard is used
    recordings = models.FloatField(default=0) #how much is the course recorded
    teacher_accessibility = models.FloatField(default=0) #how much is the teacher accessible

    #Student feedbacks
    lectures_fb = models.FloatField(default=0)
    subject_type_fb = models.FloatField(default=0)
    interactions_fb = models.FloatField(default=0)
    blackboard_fb = models.FloatField(default=0)
    recordings_fb = models.FloatField(default=0)
    teacher_accessibility_fb = models.FloatField(default=0)

    def generate_fuzzy_rules(self, variables, FS):
        values = dict(FS._lvs.items())
        rules = []
        for name, type in variables.items():
            Rule = type()
            value = getattr(self, name, None)

            test = Rule.format(self.pk, name, value, values[name])

            rules.extend(test)
        return rules

    def update_student_feeback(self, data):
        self.feedback_count += 1

        self.lectures_fb += data['lectures']
        self.subject_type_fb += data['subject_type']
        self.interactions_fb += data['interactions']
        self.blackboard_fb += data['blackboard']
        self.recordings_fb += data['recordings']
        self.teacher_accessibility_fb += data['teacher_accessibility']

        self.save()

class Track(models.Model):
    code = models.CharField(primary_key=True, unique=True, blank=False, max_length=5)
    numeric_code = models.IntegerField(default=0)
    name = models.CharField(unique=True, blank=False, max_length=255)
    description = models.TextField()

class Comment(models.Model):
    username = models.CharField(default="anonymous", max_length=255)
    comment = models.TextField()
    course = models.ForeignKey(to=Course, related_name='comments', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
