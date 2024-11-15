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

    #Fuzzy parameters
    evaluation = models.FloatField(default=0)
    university = models.FloatField(default=0)
    course_type = models.FloatField(default=0)
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
        'tracks',
        'lectures',
        'subject_type',
        'interactions',
        'blackboard',
        'recordings',
        'teacher_accessibility',
    ]

    def generate_fuzzy_rules(self, variables, FS):
        values = dict(FS._lvs.items())
        rules = []
        for var in self.fuzzy_variables:
            Rule = variables[var]()
            attr = getattr(self, var, None)
            title = self.pk
            fuzzy_var_name = var
            fuzzy_var_value = attr
            lvs = values[var]

            rules.extend(Rule.format(title, fuzzy_var_name, fuzzy_var_value, lvs))
        return rules


class Track(models.Model):
    code = models.CharField(primary_key=True, unique=True, blank=False, max_length=5)
    name = models.CharField(unique=True, blank=False, max_length=255)
    description = models.TextField()


