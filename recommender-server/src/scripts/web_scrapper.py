import requests
from bs4 import BeautifulSoup

URL = 'https://mcs.unibnf.ch/program/courses-timetable/course-list/'



if __name__ == '__main__':
    course_list_page = requests.get(URL)
    course_list_soup = BeautifulSoup(course_list_page.content, 'html.parser')

    tables = course_list_soup.find_all(id='course-list-table')

    courses = []

    track_index = 0
    for t in tables:
        tr = t.find_all('tr')
        course_index = 1
        course_length = len(tr) - 1
        for row in tr[1:]:
            current = row.find_all('td')[1].find('a', href=True)
            course_details = {}
            url = current['href']
            name = current.next_element
            print(f'Track: {track_index}: Course: {course_index}/{course_length}: {name}...')

            course_page = requests.get(current['href'])
            course_soup = BeautifulSoup(course_page.content, 'html.parser')

            course_tables = course_soup.find_all('table', class_='course-details-table')

            details_cells = course_tables[0].find_all('td', class_='course-details-content')
            teaching_cells = course_tables[1].find_all('td', class_='course-details-content')
            schedule_cells = course_tables[2].find_all('td', class_='course-details-content')
            evaluation_cells = course_tables[2].find_all('td', class_='course-details-content')


            codes = details_cells[0].contents
            if len(codes) > 1:
                codes.pop(1)
                codes[1] = codes[1][2:]

            course_type = details_cells[1].next_element
            site = details_cells[3].next_element

            tracks = []
            for a in details_cells[4].find_all('a', href=True):
                tracks.append(a.next_element.split('–')[0].strip())

            semester = details_cells[5].next_element

            teachers = []
            for a in teaching_cells[1].find_all('a', href=True):
                teachers.append(a.next_element)

            course_period = schedule_cells[0].next_element
            course_schedule = ''

            if course_period == 'Weekly':
                course_schedule = schedule_cells[1].next_element

            courses.append(course_details)

            course_index += 1
        track_index += 1

