from models.form import *


def fuzzy(form: FormRequest):
    if form.a > 10:
        return FormResponse(response='a>10')
    return FormResponse(response='a<=10')