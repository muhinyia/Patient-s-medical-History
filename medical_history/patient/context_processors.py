from .counties import Counties, Genders


def counties(request):
    return {'counties': Counties}


def genders(request):
    return {'genders': Genders}
