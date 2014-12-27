# coding: utf8
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers  import reverse

from polls.models import *
# Create your views here.

def index(request):
    latestQuestionsList = Question.objects.order_by('-pubDate')[:5]
    context = {
        'latestQuestionsList': latestQuestionsList
    }
    return render(request, 'index.html',context)

def details(request,questionId):
    question = get_object_or_404(Question, pk=questionId)
    return render(request, 'details.html', {'question':question})

def results(request,questionId):
    question = get_object_or_404(Question,pk=questionId)
    return render(request,'results.html',{
        'question':question
    })
def vote (request, questionId):
    p = get_object_or_404(Question,pk=questionId)
    try:
        selectedChoice = p.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render(request, 'detail.html',{
            'question':p,
            'error_message': "No has seleccionado ninguna"
        })
    else:
        selectedChoice.votes += 1;
        selectedChoice.save()
        return HttpResponseRedirect(reverse('results', args=(p.id,)))
