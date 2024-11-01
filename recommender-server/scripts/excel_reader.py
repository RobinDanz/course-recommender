import pandas as pd
import json

out = []

def parse_evaluation(str: str):
    evaluation = {
        'continuous': 1,
        '': 2,
        'written': 2,
        'oral': 3,
    }
    return evaluation[str.split(' ')[0]]

if __name__ == '__main__':

    file_name = 'data/courses_list_2425.xlsx'
    df = pd.read_excel(file_name)
    df.fillna({
        'Evaluation Type': '',
        'Description': ''
    }, inplace=True)

    model = 'courses.course'

    for i in range(len(df)):
        dct = {
            'model': model,
            'pk': i+1,
            'fields': {
                'title': df.Title[i],
                'day': 1,
                'type': 1,
                'site': 1,
                'code': 1,
                'start': None,
                'end': None,
                'track': 1,
                'semester': 1, 
                'description': df.Description[i],
                'url': '',
                'evaluation': parse_evaluation(df['Evaluation Type'][i]),
                'university': 0,
                'course_type': 0,
                'track': 0,
                'lectures': 0, 
                'subject_type': 0,
                'interactions': 0,
                'blackboard': 0,
                'recordings': 0,
                'teacher_accessibility': 0,
            }
        }

        out.append(dct)

    with open('src/fixtures/courses.json', 'w') as f:
        json_dump = json.dumps(out)
        f.write(json_dump)
    







    