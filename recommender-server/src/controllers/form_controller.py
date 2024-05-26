from models.form import *
from models.course import *
import simpful as sf
import numpy as np
from controllers.rules import RULES

courses = ['QMPECS', 'Concurrency', 'AppliedOptimization', 'MLDM', 'SocialComputing', 'FuzzySets2']
full_names = ['Quantitative Methods of Performance Evaluation for Computing Systems', 
              'Concurrency: Multi-core Programming and Data Processing', 
              'Applied Optimization',
              'Machine Learning and Data Mining',
              'Seminar Social Computing',
              'Fuzzy Sets and Systems II']
VARIABLES = ['Evaluation', 'University', 'CourseType', 'Track', 'Lectures', 'SubjectType', 'Interactions', 'Blackboard', 'Recordings', 'TeacherAccessibilty']

def fuzzy_set_variables(form: FormRequest, FS: sf.FuzzySystem) -> dict:
    """Function setting the values of the different variables of the fuzzy system.

    Args:
        form (FormRequest): Answers from the form 
        FS (sf.FuzzySystem): Fuzzy system to use

    Returns:
        dict: Dictionnary with percent of recommendation for each course
    """

    # Fetches de rules of the fuzzy system 
    rules = FS.get_rules()

    # For each variable with more than one choice possible we reduce the weight of the concerned rules and take the mean answer.
    # First we control if there are more than one answer
    if len(form.evaluation) > 1:
        # We caculate the mean 
        mean_eval = np.mean(form.evaluation)
        # We calculate the weight in proportion to how many they choose
        weight = 1- len(form.evaluation)/4
        # Then we add the weight to the rules that are concerned by this variable, in this case 'Evaluation'
        for i in range(len(rules)):
            if str(rules[i]).find('Evaluation') != -1: # If it does not find 'Evaluation' it returns -1
                new_rule = ' '.join([rules[i], f'WEIGHT {weight}']) 
                FS.replace_rule(i, new_rule)
        # Then set the variable to the mean value
        FS.set_variable('Evaluation', mean_eval)
    else:
        # Else we set the variable normally
        FS.set_variable('Evaluation', form.evaluation[0])

    # University variable
    if len(form.university) > 1:
        mean_eval = np.mean(form.university)
        weight = 1- len(form.university)/3
        for i in range(len(rules)):
            if str(rules[i]).find('University') != -1:
                new_rule = ' '.join([rules[i], f'WEIGHT {weight}']) 
                FS.replace_rule(i, new_rule)
        FS.set_variable('University', mean_eval)
    else:
        FS.set_variable('University', form.university[0])

    # CourseType variable
    if len(form.courseType) > 1:
        mean_eval = np.mean(form.courseType)
        weight = 1- len(form.courseType)/2
        for i in range(len(rules)):
            if str(rules[i]).find('CourseType') != -1:
                new_rule = ' '.join([rules[i], f'WEIGHT {weight}']) 
                FS.replace_rule(i, new_rule)
        FS.set_variable('CourseType', mean_eval)
    else:
        FS.set_variable('CourseType', form.courseType[0])

    # Track variable
    if len(form.track) > 1:
        mean_eval = np.mean(form.track)
        weight = 1- len(form.track)/7
        for i in range(len(rules)):
            if str(rules[i]).find('Track') != -1:
                new_rule = ' '.join([rules[i], f'WEIGHT {weight}']) 
                FS.replace_rule(i, new_rule)
        FS.set_variable('Track', mean_eval)
    else:
        FS.set_variable('Track', form.track[0])

    # Lectures variable
    if len(form.lectures) > 1:
        mean_eval = np.mean(form.lectures)
        weight = 1- len(form.lectures)/5
        for i in range(len(rules)):
            if str(rules[i]).find('Lectures') != -1:
                new_rule = ' '.join([rules[i], f'WEIGHT {weight}']) 
                FS.replace_rule(i, new_rule)
        FS.set_variable('Lectures', mean_eval)
    else:
        FS.set_variable('Lectures', form.lectures[0])

    # These variable are sliders and only one answer is possible between 0 and 100
    FS.set_variable('SubjectType', form.subjectType)
    FS.set_variable('Interactions', form.interactions)
    FS.set_variable('Blackboard', form.blackboard)
    FS.set_variable('Recordings', form.recordings)
    FS.set_variable('TeacherAccessibilty', form.teacherAccessibilty)

    # Calculate the inference 
    outputs = FS.inference()

    # Sorts the output dictionnary
    sorted_outputs = dict(sorted(outputs.items(), key=lambda item: item[1], reverse=True))
    
    # Changes the names of the courses to their full names
    full_dict = {}
    for key in sorted_outputs.keys():
        full_dict[full_names[courses.index(key)]] = sorted_outputs[key]

    return full_dict


def create_fuzzy() -> sf.FuzzySystem:
    """Function creating the fuzzy system.

    Returns:
        sf.FuzzySystem: Returns a fuzzy system for the course recommender
    """

    # Creating the fuzzy system
    FS = sf.FuzzySystem(show_banner=False)

    # Evaluation: variable between 0 and 3
    E_1 = sf.CrispSet(a=0, b=0.5, term='project')
    E_2 = sf.CrispSet(a=0.5, b=1.5, term='continuous')
    E_3 = sf.CrispSet(a=1.5, b=2.5, term='written')
    E_4 = sf.CrispSet(a=2.5, b=3, term='oral')
    evaluation = sf.LinguisticVariable([E_1, E_2, E_3, E_4], universe_of_discourse=[0, 3])
    FS.add_linguistic_variable('Evaluation', evaluation)

    # University: variable between 0 and 2
    U_1 = sf.CrispSet(a=0, b=0.5, term='bern')
    U_2 = sf.CrispSet(a=0.5, b=1.5, term='fribourg')
    U_3 = sf.CrispSet(a=1.5, b=2, term='neuchatel')
    university = sf.LinguisticVariable([U_1, U_2, U_3], universe_of_discourse=[0, 2])
    FS.add_linguistic_variable('University', university)

    # Course type: variable between 0 and 1
    C_1 = sf.CrispSet(a=0, b=0.5, term='seminar')
    C_2 = sf.CrispSet(a=0.5, b=1, term='course')
    course_type = sf.LinguisticVariable([C_1, C_2], universe_of_discourse=[0, 1])
    FS.add_linguistic_variable('CourseType', course_type)

    # Track: variable between 0 and 6
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
    FS.add_linguistic_variable('Interactions', LV) # none to always
    FS.add_linguistic_variable('Blackboard', LV) # no use of the blackboard to always
    FS.add_linguistic_variable('Recordings', LV) # no recordings available to always
    FS.add_linguistic_variable('TeacherAccessibilty', LV) # never accessible to always

    # Output
    FS.set_crisp_output_value('notRecommended', 0)
    FS.set_crisp_output_value('recommended', 100)

    # IF/THEN rules
    FS.add_rules(RULES)

    return FS


# Test answers
# test_FS = create_fuzzy()

# test_FS.set_variable('Evaluation', 2)
# test_FS.set_variable('University', 2)
# test_FS.set_variable('CourseType', 1)
# test_FS.set_variable('Track', 1)
# test_FS.set_variable('Lectures', 25)
# test_FS.set_variable('SubjectType', 75)
# test_FS.set_variable('Interactions', 25)
# test_FS.set_variable('Blackboard', 0)
# test_FS.set_variable('Recordings', 100)
# test_FS.set_variable('TeacherAccessibilty', 75)

# outputs = test_FS.inference(verbose=False)
# sorted_outputs = dict(sorted(outputs.items(), key=lambda item: item[1], reverse=True))

# # Shows the used rules
# # for i, value in enumerate(test_FS.get_firing_strengths()):
# #         if value:
# #             print(f"- {RULES[i]}")

# print(f"Sorted outputs: {sorted_outputs}")
# full_dict = {}
# for key in sorted_outputs.keys():
#     full_dict[full_names[courses.index(key)]]= sorted_outputs[key]
# print(full_dict)