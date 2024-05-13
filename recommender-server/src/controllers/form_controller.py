from models.form import *
import simpful as sf
import numpy as np


def fuzzy(form: FormRequest):
    """
    test
    """
    if form.a > 10:
        return FormResponse(response='a>10')
    return FormResponse(response='a<=10')

FS = sf.FuzzySystem()
Courses = ['SocialComputing', 'Concurrency', 'FuzzySets2']
VARIABLES = ['Evaluation', 'University', 'CourseType', 'Track', 'Lectures', 'SubjectType', 'Interactions', 'Blackboard', 'Recordings', 'TeacherAccessibilty']

# Evaluation
E_1 = sf.CrispSet(a=0., b=0.25, term='project')
E_2 = sf.CrispSet(a=0.25, b=0.5, term='continuous')
E_3 = sf.CrispSet(a=0.5, b=0.75, term='written')
E_4 = sf.CrispSet(a=0.75, b=1., term='oral')
evaluation = sf.LinguisticVariable([E_1, E_2, E_3, E_4], universe_of_discourse=[0., 1.])
FS.add_linguistic_variable('Evaluation', evaluation)

# University
U_1 = sf.CrispSet(a=0., b=0.33, term='bern')
U_2 = sf.CrispSet(a=0.33, b=0.66, term='fribourg')
U_3 = sf.CrispSet(a=0.66, b=1., term='neuchatel')
university = sf.LinguisticVariable([U_1, U_2, U_3], universe_of_discourse=[0., 1.])
FS.add_linguistic_variable('University', university)

# Course type
C_1 = sf.CrispSet(a=0., b=0.5, term='seminar')
C_2 = sf.CrispSet(a=0.5, b=1., term='course')
course_type = sf.LinguisticVariable([C_1, C_2], universe_of_discourse=[0., 1.])
FS.add_linguistic_variable('CourseType', course_type)

# Track
T_1 = sf.CrispSet(a=0., b=0.14, term='T0')
T_2 = sf.CrispSet(a=0.14, b=0.29, term='T1')
T_3 = sf.CrispSet(a=0.29, b=0.43, term='T2')
T_4 = sf.CrispSet(a=0.43, b=0.57, term='T3')
T_5 = sf.CrispSet(a=0.57, b=0.71, term='T4')
T_6 = sf.CrispSet(a=0.71, b=0.86, term='T5')
T_7 = sf.CrispSet(a=0.86, b=1., term='T6')
track = sf.LinguisticVariable([T_1, T_2, T_3, T_4, T_5, T_6, T_7], universe_of_discourse=[0., 1.])
FS.add_linguistic_variable('Track', track)

# Linguistic variable for the fuzzy variables
LV = sf.AutoTriangle(5, terms=['none', 'some', 'middle', 'regularly', 'always'], universe_of_discourse=[0., 1.])
FS.add_linguistic_variable('Lectures', LV)
FS.add_linguistic_variable('SubjectType', LV)
FS.add_linguistic_variable('Interactions', LV)
FS.add_linguistic_variable('Blackboard', LV)
FS.add_linguistic_variable('Recordings', LV)
FS.add_linguistic_variable('TeacherAccessibilty', LV)

# Output
"""
LO = sf.AutoTriangle(len(Courses), terms=[course for course in Courses], universe_of_discourse=[0., 1.])
FS.add_linguistic_variable('Course', LO)
"""
LO = sf.AutoTriangle(3, terms=['notRecommended', 'okay', 'recommended'], universe_of_discourse=[0., 1.])
for course in Courses:
    FS.add_linguistic_variable(course, LO)

"""
FS.set_crisp_output_value('SocialComputing', 0.0)
FS.set_crisp_output_value('Concurrency', 1.0)
"""

# IF/THEN rules
"""
R_1 = "IF (Evaluation IS project) AND (University IS fribourg) AND (CourseType IS seminar) AND (Track IS T5) AND (Lectures IS always) AND (SubjectType IS always) AND (Interactions IS some) AND (Blackboard IS none) AND (Recordings IS none) AND (TeacherAccessibilty IS middle) THEN (Course IS SocialComputing)"
R_2 = "IF (Evaluation IS written) AND (University IS neuchatel) AND (CourseType IS course) AND (Track IS T1) AND (Lectures IS some) AND (SubjectType IS regularly) AND (Interactions IS some) AND (Blackboard IS none) AND (Recordings IS always) AND (TeacherAccessibilty IS regularly) THEN (Course IS Concurrency)"
FS.add_rules([R_1, R_2])
"""
FS.add_rules_from_file('/Users/michelefischer/MA1P/SocialComputing/course-recommender/recommender-server/src/controllers/rules.txt')

# Test with a random answer
"""
FS.set_variable('Evaluation', 0.7)
FS.set_variable('University', 0.75)
FS.set_variable('CourseType', 0.55)
FS.set_variable('Track', 0.95)
FS.set_variable('Lectures', 0.1)
FS.set_variable('SubjectType', 0.75)
FS.set_variable('Interactions', 0.76)
FS.set_variable('Blackboard', 0.90)
FS.set_variable('Recordings', 0.90)
FS.set_variable('TeacherAccessibilty', 0.84)
"""
for variable in VARIABLES:
    FS.set_variable(variable, np.random.random(), verbose=False)

# Output
print(FS.Mamdani_inference([course for course in Courses], verbose=False))
