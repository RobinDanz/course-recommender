from models.form import *


def fuzzy(form: FormRequest):
    """
    test
    """
    if form.a > 10:
        return FormResponse(response='a>10')
    return FormResponse(response='a<=10')