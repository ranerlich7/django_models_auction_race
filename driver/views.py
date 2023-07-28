from django.http import HttpResponse
from django.shortcuts import render

from driver.models import Driver

# Create your views here.

# def index():
    # Driver.objects.all()
    
def drivers(request):
    # get all drivers from DB
    all_drivers = Driver.objects.all()
    mystr = ""
    for driver in all_drivers:
        # add driver str
        mystr += str(driver)
        # add all races for this driver - driver.race_set.all()
        mystr += str([str(race) for race in driver.race_set.all()])
        mystr += "<br>"
    # return all drivers as html
    return HttpResponse(f"This is a list of drivers!<br>{mystr}")
    