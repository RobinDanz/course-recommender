from courses.models import Course

class Rule:
    """
    Rule for crisp variables
    """
    def __init__(self):
        self.template = "IF (%s IS %s) THEN %s IS recommended"
        self.not_template = "IF (NOT(%s IS %s)) THEN %s IS notRecommended"

    def format(self, title, fuzzy_var, linguistic_var, lvs):
        return_str = self.template % (fuzzy_var, self.get_term(linguistic_var, lvs), title)
        return_not_str = self.not_template % (fuzzy_var, self.get_term(linguistic_var, lvs), title)
        return [return_str, return_not_str]
    
    def get_term(self, value, lvs):
        lvs = lvs.get_values(value)
        return max(lvs, key = lambda i: lvs[i])

class TrackRule(Rule):
    """
    Rule specific to track
    """
    def __init__(self):
        self.template = "IF %s THEN %s IS recommended"
        self.not_template = "IF %s THEN %s IS notRecommended"
        self.existing_tracks = [
            'T0',
            'T1',
            'T2',
            'T3',
            'T4',
            'T5',
            'T6',
        ]

    def format(self, title, fuzzy_var, linguistic_var, lvs):
        
        tracks = [str(track) for track in linguistic_var.all().values_list('code', flat=True)]
        not_tracks =[t for t in self.existing_tracks if t not in tracks]

        base = '(tracks IS %s)'
        out_recommended = ' OR '.join([base % t for t in tracks])
        out_not_recommended = ' OR '.join([base % t for t in not_tracks])

        return_str_recommended = self.template % (out_recommended, title)
        return_str_not_recommended = self.not_template % (out_not_recommended, title)
        return [return_str_recommended, return_str_not_recommended]

class FuzzyRule(Rule):
    """
    Rule for fuzzy variables
    """
    def __init__(self):
        self.template = "IF (%s IS %s) OR (%s IS %s) THEN %s IS recommended"
        self.middle_template = "IF (%s IS %s) THEN %s IS medium"
        self.not_template = "IF (%s IS %s) OR (%s IS %s) THEN %s IS notRecommended"
        
    def format(self, title, fuzzy_var, linguistic_var, lvs):
        vars = list(self.get_term(linguistic_var, lvs).keys())

        r1 = self.template % (fuzzy_var, vars[0], fuzzy_var, vars[1], title)
        r2 = self.middle_template % (fuzzy_var, vars[2], title)
        r3 = self.not_template % (fuzzy_var, vars[3], fuzzy_var, vars[4], title)

        return [r1, r2, r3]

    def get_term(self, value, lvs):
        values = lvs.get_values(value)
        return dict(sorted(values.items(), key=lambda item: item[1], reverse=True))

VARIABLES = {
    'evaluation': Rule,
    'university': Rule,
    'course_type': Rule,
    'tracks': TrackRule,
    'lectures': FuzzyRule,
    'subject_type': FuzzyRule,
    'interactions': FuzzyRule,
    'blackboard': FuzzyRule,
    'recordings': FuzzyRule,
    'teacher_accessibility': FuzzyRule,
}

def generate_rules(FS):
    courses = Course.objects.all()
    rules = []
    for course in courses:
        rules.extend(course.generate_fuzzy_rules(VARIABLES, FS))
    FS.add_rules(rules)
