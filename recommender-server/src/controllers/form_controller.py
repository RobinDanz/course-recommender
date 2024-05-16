from models.form import *
import simpful as sf
import numpy as np


FS = sf.FuzzySystem()
courses = ['SocialComputing', 'Concurrency', 'FuzzySets2', 'test']
VARIABLES = ['Evaluation', 'University', 'CourseType', 'Track', 'Lectures', 'SubjectType', 'Interactions', 'Blackboard', 'Recordings', 'TeacherAccessibilty']

def fuzzy_set_variables(form: FormRequest):
    """
    test
    """
    rules = FS.get_rules()
    if len(form.evaluation) > 1:
        mean_eval = np.mean(form.evaluation)
        weight = 1- len(form.evaluation)/4
        for i in len(rules):
            if str(rules[i]).find('Evaluation') != -1:
                new_rule = ' '.join([rules[i], f'WEIGHT {weight}']) 
                FS.replace_rule(i, new_rule)
        FS.set_variable('Evaluation', mean_eval)
    else:
        FS.set_variable('Evaluation', form.evaluation[0])

    if len(form.university) > 1:
        mean_eval = np.mean(form.university)
        weight = 1- len(form.university)/3
        for i in len(rules):
            if str(rules[i]).find('University') != -1:
                new_rule = ' '.join([rules[i], f'WEIGHT {weight}']) 
                FS.replace_rule(i, new_rule)
        FS.set_variable('University', mean_eval)
    else:
        FS.set_variable('University', form.university[0])

    if len(form.courseType) > 1:
        mean_eval = np.mean(form.courseType)
        weight = 1- len(form.courseType)/2
        for i in len(rules):
            if str(rules[i]).find('CourseType') != -1:
                new_rule = ' '.join([rules[i], f'WEIGHT {weight}']) 
                FS.replace_rule(i, new_rule)
        FS.set_variable('CourseType', mean_eval)
    else:
        FS.set_variable('CourseType', form.courseType[0])

    if len(form.track) > 1:
        mean_eval = np.mean(form.track)
        weight = 1- len(form.track)/7
        for i in len(rules):
            if str(rules[i]).find('Track') != -1:
                new_rule = ' '.join([rules[i], f'WEIGHT {weight}']) 
                FS.replace_rule(i, new_rule)
        FS.set_variable('Track', mean_eval)
    else:
        FS.set_variable('Track', form.track[0])

    if len(form.lectures) > 1:
        mean_eval = np.mean(form.lectures)
        weight = 1- len(form.lectures)/5
        for i in len(rules):
            if str(rules[i]).find('Lectures') != -1:
                new_rule = ' '.join([rules[i], f'WEIGHT {weight}']) 
                FS.replace_rule(i, new_rule)
        FS.set_variable('Lectures', mean_eval)
    else:
        FS.set_variable('Lectures', form.lectures[0])

    FS.set_variable('SubjectType', form.subjectType)
    FS.set_variable('Interactions', form.interactions)
    FS.set_variable('Blackboard', form.blackboard)
    FS.set_variable('Recordings', form.recordings)
    FS.set_variable('TeacherAccessibilty', form.teacherAccessibilty)
    return FS.Mamdani_inference([course for course in courses], verbose=False)


# Evaluation 
E_1 = sf.CrispSet(a=0, b=0.5, term='project')
E_2 = sf.CrispSet(a=0.5, b=1.5, term='continuous')
E_3 = sf.CrispSet(a=1.5, b=2.5, term='written')
E_4 = sf.CrispSet(a=2.5, b=3, term='oral')
evaluation = sf.LinguisticVariable([E_1, E_2, E_3, E_4], universe_of_discourse=[0, 3])
FS.add_linguistic_variable('Evaluation', evaluation)

# University
U_1 = sf.CrispSet(a=0, b=0.5, term='bern')
U_2 = sf.CrispSet(a=0.5, b=1.5, term='fribourg')
U_3 = sf.CrispSet(a=1.5, b=2, term='neuchatel')
university = sf.LinguisticVariable([U_1, U_2, U_3], universe_of_discourse=[0, 2])
FS.add_linguistic_variable('University', university)

# Course type
C_1 = sf.CrispSet(a=0, b=0.5, term='seminar')
C_2 = sf.CrispSet(a=0.5, b=1, term='course')
course_type = sf.LinguisticVariable([C_1, C_2], universe_of_discourse=[0, 1])
FS.add_linguistic_variable('CourseType', course_type)

# Track
T_1 = sf.CrispSet(a=0, b=0.5, term='T0')
T_2 = sf.CrispSet(a=0.5, b=1.5, term='T1')
T_3 = sf.CrispSet(a=1.5, b=2.5, term='T2')
T_4 = sf.CrispSet(a=2.5, b=3.5, term='T3')
T_5 = sf.CrispSet(a=3.5, b=4.5, term='T4')
T_6 = sf.CrispSet(a=4.5, b=5.5, term='T5')
T_7 = sf.CrispSet(a=5.5, b=6, term='T6')
track = sf.LinguisticVariable([T_1, T_2, T_3, T_4, T_5, T_6, T_7], universe_of_discourse=[0, 6])
FS.add_linguistic_variable('Track', track)

# Linguistic variable for the fuzzy variables
LV = sf.AutoTriangle(5, terms=['none', 'some', 'middle', 'regularly', 'always'], universe_of_discourse=[0, 100])
FS.add_linguistic_variable('Lectures', LV) # only lectures,	lectures + some exercices,	lectures + exercices,	lectures + project,	no lectures + project
FS.add_linguistic_variable('SubjectType', LV)  # theoretical to practical
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
for course in courses:
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
eva = [0, 1, 3, 4]
rules = FS.get_rules()
if len(eva) > 1:
    mean_eval = np.mean(eva)
    weight = 1- len(eva)/4
    for i in range(len(rules)):
        if str(rules[i]).find('Evaluation') != -1:
            new_rule = ' '.join([rules[i], f'WEIGHT {weight}']) 
            FS.replace_rule(i, new_rule, verbose=True)
    FS.set_variable('Evaluation', mean_eval)
else:
        FS.set_variable('Evaluation', eva[0])

FS.set_variable('University', 1)
FS.set_variable('CourseType', 1)
FS.set_variable('Track', 5)
FS.set_variable('Lectures', 20)
FS.set_variable('SubjectType', 50)
FS.set_variable('Interactions', 76)
FS.set_variable('Blackboard', 90)
FS.set_variable('Recordings', 90)
FS.set_variable('TeacherAccessibilty', 84)

"""
for variable in VARIABLES:
    FS.set_variable(variable, np.random.random(), verbose=False)
"""

# Output
print(FS.Mamdani_inference([course for course in courses], verbose=False))
