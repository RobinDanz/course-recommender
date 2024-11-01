from django.db import models
from fuzzy.logic import fuzzy_controller

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

    #Fuzzy parameters
    evaluation = models.FloatField(default=0)
    university = models.FloatField(default=0)
    course_type = models.FloatField(default=0)
    track = models.FloatField(default=0)
    lectures = models.FloatField(default=0)
    subject_type = models.FloatField(default=0)
    interactions = models.FloatField(default=0)
    blackboard = models.FloatField(default=0)
    recordings = models.FloatField(default=0)
    teacher_accessibility = models.FloatField(default=0)

    fuzzy_variables = [
        'evaluation',
        'university',
        'course_type',
        'track',
        'lectures',
        'subject_type',
        'interactions',
        'blackboard',
        'recordings',
        'teacher_accessibility',
    ]

    def generate_fuzzy_rules(self, variables):
        FS = fuzzy_controller.create_fuzzy()
        for var in self.fuzzy_variables:
            RuleKlass = variables[var]()
            print(type(FS.get_fuzzy_sets('University')[0]))
            print(self.title)
            attr = getattr(self, var, None)

            print(attr)

            if attr:
                params = (f'({var} IS #loadvalfrommodel#)', f'({self.title} IS recommended)')
                print(RuleKlass.template % params)



