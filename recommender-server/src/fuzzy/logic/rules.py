from courses.models import Course

class Rule:
    def __init__(self):
        self.template = "IF (%s IS %s) THEN %s IS recommended"
        self.not_template = "IF (NOT(%s IS %s)) THEN %s IS notRecommended"

    def format(self, title, fuzzy_var, linguistic_var, lvs):
        return_str = self.template % (fuzzy_var, self.get_term(linguistic_var, lvs), title)
        return_not_str = self.not_template % (fuzzy_var, self.get_term(linguistic_var, lvs), title)
        return [return_str, return_not_str]
    
    def get_term(self, value, lvs):
        test = lvs.get_values(value)
        return max(test, key = lambda i: test[i])

class TrackRule(Rule):
    def __init__(self):
        self.template = "IF %s THEN %s IS recommended"

    def format(self, title, fuzzy_var, linguistic_var, lvs):
        tracks = [str(track) for track in linguistic_var.all().values_list('code', flat=True)]

        test = '(tracks IS %s)'
        out = ''
        if len(tracks) == 1:
            out = test % tracks[0]
        else:
            t1 = test % tracks[0]
            t2 = test % tracks[1]
            out = t1 + ' OR ' + t2
        
        return_str = self.template % (out, title)
        return [return_str]

VARIABLES = {
    'evaluation': Rule,
    'university': Rule,
    'course_type': Rule,
    'tracks': TrackRule,
    'lectures': Rule,
    'subject_type': Rule,
    'interactions': Rule,
    'blackboard': Rule,
    'recordings': Rule,
    'teacher_accessibility': Rule,
}

def generate_rules(FS):
    courses = Course.objects.all()
    rules = []
    for course in courses:
        rules.extend(course.generate_fuzzy_rules(VARIABLES, FS))
    FS.add_rules(rules)
