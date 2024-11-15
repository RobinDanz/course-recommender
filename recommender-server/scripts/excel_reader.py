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

def format_day(str: str):
    day = str.split(',')[0]

    days = ['Monday', 'Thursday', 'Wednesday', 'Tuesday', 'Friday']
    if day not in days:
        return 0

    return days.index(day) + 1

def format_start_time(str: str):
    if str == '-':
        return None
    time = str.split(',')[1]
    start_time = time.split('-')[0].strip() + ':00'
    return start_time

def format_end_time(str: str):
    if str == '-':
        return None
    time = str.split(',')[1]
    end_time = time.split('-')[0].strip() + ':00'
    return end_time

def format_tracks(str: str):
    tracks = str.split(',')
    return [t.strip() for t in tracks]

def parse_course_type(str: str):
    types = ['Course', 'Seminar']

    return types.index(str)

def parse_semester(str: str):
    semesters = ['SS', 'AS']

    return semesters.index(str)

def parse_university(str: str):
    uni = str.split(' ')[2]
    universities = ['Bern', 'Fribourg', 'Neuchâtel']

    return universities.index(uni)

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
                'day': format_day(df.Schedule[i]),
                'type': parse_course_type(df.Type[i]),
                'site': parse_university(df.Affiliation[i]),
                'code': df.Code[i],
                'start': format_start_time(df.Schedule[i]),
                'end': format_end_time(df.Schedule[i]),
                'semester': parse_semester(df.Semester[i]), 
                'description': df.Description[i],
                'url': '',
                'evaluation': parse_evaluation(df['Evaluation Type'][i]),
                'university': parse_university(df.Affiliation[i]),
                'course_type': parse_course_type(df.Type[i]),
                'lectures': 0, 
                'subject_type': 0,
                'interactions': 0,
                'blackboard': 0,
                'recordings': 0,
                'teacher_accessibility': 0,
                'tracks': format_tracks(df.Tracks[i])
            }
        }

        out.append(dct)

    with open('src/courses/fixtures/courses.json', 'w') as f:
        json_dump = json.dumps(out)
        f.write(json_dump)
    







    