from django.http import HttpResponse
from datetime import datetime

def hello(request):
    if request.method == "GET":
        return HttpResponse("Hello! It's my pastries project")


def now_date(request):
    if request.method == "GET":
        now = datetime.now()
        return HttpResponse("Current date and time: " + now.strftime("%Y-%m-%d %H:%M:%S"))


def goodbye(request):
    if request.method == "GET":
        return HttpResponse("Goodbye dear user!")