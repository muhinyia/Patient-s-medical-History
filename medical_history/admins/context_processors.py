from .titles import Titles, Levels
from facilities.models import Facility


def titles(request):
    return {'titles': Titles}


def levels(request):
    return {'levels': Levels}


def facilities(request):
    facilities = Facility.objects.filter(is_registered=True)

    return {'facilities': facilities}
