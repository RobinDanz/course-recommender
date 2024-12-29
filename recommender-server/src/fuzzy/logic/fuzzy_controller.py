import simpful as sf
import numpy as np
from fuzzy.logic import rules

class SingletonMeta(type):
    """
    A Singleton metaclass that ensures a class has only one instance.
    """
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class FuzzyController(metaclass=SingletonMeta):
    def __init__(self):
        self.FS = self.create_fuzzy()

    def create_fuzzy(self):
        # Creating the fuzzy system
        FS = sf.FuzzySystem(show_banner=False)

        # evaluation: variable between 0 and 3
        E_1 = sf.CrispSet(a=0, b=0.5, term='project')
        E_2 = sf.CrispSet(a=0.5, b=1.5, term='continuous')
        E_3 = sf.CrispSet(a=1.5, b=2.5, term='written')
        E_4 = sf.CrispSet(a=2.5, b=3, term='oral')
        evaluation = sf.LinguisticVariable([E_1, E_2, E_3, E_4], universe_of_discourse=[0, 3])
        FS.add_linguistic_variable('evaluation', evaluation)

        # university: variable between 0 and 2
        U_1 = sf.CrispSet(a=0, b=0.5, term='bern')
        U_2 = sf.CrispSet(a=0.5, b=1.5, term='fribourg')
        U_3 = sf.CrispSet(a=1.5, b=2, term='neuchatel')
        university = sf.LinguisticVariable([U_1, U_2, U_3], universe_of_discourse=[0, 2])

        FS.add_linguistic_variable('university', university)

        # Course type: variable between 0 and 1
        C_1 = sf.CrispSet(a=0, b=0.5, term='seminar')
        C_2 = sf.CrispSet(a=0.5, b=1, term='course')
        course_type = sf.LinguisticVariable([C_1, C_2], universe_of_discourse=[0, 1])
        FS.add_linguistic_variable('course_type', course_type)

        # tracks: variable between 0 and 6
        T_1 = sf.CrispSet(a=0, b=0.5, term='T0')
        T_2 = sf.CrispSet(a=0.5, b=1.5, term='T1')
        T_3 = sf.CrispSet(a=1.5, b=2.5, term='T2')
        T_4 = sf.CrispSet(a=2.5, b=3.5, term='T3')
        T_5 = sf.CrispSet(a=3.5, b=4.5, term='T4')
        T_6 = sf.CrispSet(a=4.5, b=5.5, term='T5')
        T_7 = sf.CrispSet(a=5.5, b=6, term='T6')
        track = sf.LinguisticVariable([T_1, T_2, T_3, T_4, T_5, T_6, T_7], universe_of_discourse=[0, 6])
        FS.add_linguistic_variable('tracks', track)

        # Linguistic variable for the fuzzy variables
        LV = sf.AutoTriangle(5, terms=['none', 'some', 'middle', 'regularly', 'always'], universe_of_discourse=[0, 100])
        LV_lectures = sf.AutoTriangle(5, terms=['lectures_only', 'lectures_some_exercices', 'lectures_exercices', 'lectures_project', 'project_only'], universe_of_discourse=[0, 100])
        LV_subject = sf.AutoTriangle(5, terms=['theoritical', 'theoritical_little_practical', 'theoritical_practical', 'practical_little_theoritical', 'practical'], universe_of_discourse=[0, 100])
        FS.add_linguistic_variable('lectures', LV_lectures) # only lectures,	lectures + some exercices,	lectures + exercices,	lectures + project,	no lectures + project
        FS.add_linguistic_variable('subject_type', LV_subject)  # theoretical to practical
        FS.add_linguistic_variable('interactions', LV) # none to always
        FS.add_linguistic_variable('blackboard', LV) # no use of the blackboard to always
        FS.add_linguistic_variable('recordings', LV) # no recordings available to always
        FS.add_linguistic_variable('teacher_accessibility', LV) # never accessible to always

        # Output
        FS.set_crisp_output_value('notRecommended', 0)
        FS.set_crisp_output_value('medium', 50)
        FS.set_crisp_output_value('recommended', 100)
        #LV_output = sf.AutoTriangle(3, terms=['notRecommended', 'middle', 'recommended'], universe_of_discourse=[0, 100])
        #FS.add_linguistic_variable('output', LV_output)

        # IF/THEN rules
        rules.generate_rules(FS)

        return FS

    def inference(self, form):
        """Function setting the values of the different variables of the fuzzy system.

        Args:
            form (FormRequest): Answers from the form 
            FS (sf.FuzzySystem): Fuzzy system to use

        Returns:
            dict: Dictionnary with percent of recommendation for each course
        """

        # Fetches de rules of the fuzzy system 
        rules = self.FS.get_rules()

        # For each variable with more than one choice possible we reduce the weight of the concerned rules and take the mean answer.
        # First we control if there are more than one answer
        if len(form['evaluation']) > 1:
            # We caculate the mean
            mean_eval = np.mean(form['evaluation'])
            # We calculate the weight in proportion to how many they choose
            weight = 1- len(form['evaluation'])/4
            # Then we add the weight to the rules that are concerned by this variable, in this case 'evaluation'
            for i in range(len(rules)):
                if str(rules[i]).find('evaluation') != -1: # If it does not find 'evaluation' it returns -1
                    new_rule = ' '.join([rules[i], f'WEIGHT {weight}'])
                    self.FS.replace_rule(i, new_rule)
            # Then set the variable to the mean value
            self.FS.set_variable('evaluation', mean_eval)
        else:
            # Else we set the variable normally
            self.FS.set_variable('evaluation', form['evaluation'][0])

        # university variable
        if len(form['university']) > 1:
            mean_eval = np.mean(form['university'])
            weight = 1- len(form['university'])/3
            for i in range(len(rules)):
                if str(rules[i]).find('university') != -1:
                    new_rule = ' '.join([rules[i], f'WEIGHT {weight}'])
                    self.FS.replace_rule(i, new_rule)
            self.FS.set_variable('university', mean_eval)
        else:
            self.FS.set_variable('university', form['university'][0])

        # course_type variable
        if len(form['course_type']) > 1:
            mean_eval = np.mean(form['course_type'])
            weight = 1- len(form['course_type'])/2
            for i in range(len(rules)):
                if str(rules[i]).find('course_type') != -1:
                    new_rule = ' '.join([rules[i], f'WEIGHT {weight}']) 
                    self.FS.replace_rule(i, new_rule)
            self.FS.set_variable('course_type', mean_eval)
        else:
            self.FS.set_variable('course_type', form['course_type'][0])

        # tracks variable
        if len(form['track']) > 1:
            mean_eval = np.mean(form['track'])
            weight = 1- len(form['track'])/7
            for i in range(len(rules)):
                if str(rules[i]).find('tracks') != -1:
                    new_rule = ' '.join([rules[i], f'WEIGHT {weight}']) 
                    self.FS.replace_rule(i, new_rule)
            self.FS.set_variable('tracks', mean_eval)
        else:
            self.FS.set_variable('tracks', form['track'][0])

        # These variable are sliders and only one answer is possible between 0 and 100
        self.FS.set_variable('lectures', form['lectures'])
        self.FS.set_variable('subject_type', form['subject_type'])
        self.FS.set_variable('interactions', form['interactions'])
        self.FS.set_variable('blackboard', form['blackboard'])
        self.FS.set_variable('recordings', form['recordings'])
        self.FS.set_variable('teacher_accessibility', form['teacher_accessibility'])

        # Calculate the inference 
        outputs = self.FS.inference()
        
        # Sorts the output dictionnary
        sorted_outputs = dict(sorted(outputs.items(), key=lambda item: item[1], reverse=True))
        return sorted_outputs    

    def get_linguistic_var(self, variable, value):
        lvs = dict(self.FS._lvs.items())

        values = lvs[variable].get_values(value)
        return list(dict(sorted(values.items(), key=lambda item: item[1], reverse=True)).keys())[0]

    