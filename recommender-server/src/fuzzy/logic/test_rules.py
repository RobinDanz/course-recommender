class Rule:
    def __init__(self):
        self.template = "IF %s THEN %s"

class TrackRule(Rule):
    def __init__(self):
        super().__init__()

variables = {
    'evaluation': Rule,
    'university': Rule,
    'course_type': Rule,
    'track': TrackRule,
    'lectures': Rule,
    'subject_type': Rule,
    'interactions': Rule,
    'blackboard': Rule,
    'recordings': Rule,
    'teacher_accessibility': Rule,
}

from courses.models import Course

def generate_rules():
    courses = Course.objects.filter(pk=1)
    for course in courses:
        course.generate_fuzzy_rules(variables)
