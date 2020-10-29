from django.shortcuts import render, HttpResponse
from .models import Person
from os import environ as env
# Create your views here.
def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    p = Person.objects.create(name='ranjan')
    persons = Person.objects.filter(name='ranjan')

    # just changing something
    # comment change    test
    context = {
        'usr' : env.get('POSTGRES_USER'),
        'pwd' : env.get('POSTGRES_PASSWORD'),
        'persons':persons,
        'msg': 'hello world test'
    }

    return render(request,'app/index.html',context=context)
