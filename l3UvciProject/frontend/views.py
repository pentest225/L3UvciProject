from django.http import Http404, HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
    # template = loader.get_template("site/index.html")
    # context = {
    #     "latest_question_list": 12,
    # }
    # raise Http404("Question does not exist")
    return render(request, "app_dashboard/index.html")
    

# Create your views here.
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)