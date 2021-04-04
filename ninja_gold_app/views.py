from django.shortcuts import render, redirect
from time import gmtime, strftime
import random

def index(request):
    context = {
        'time': strftime("%a, %d %b %Y %I:%M %p", gmtime())
    }
    if 'activities' not in request.session:
        request.session['activities'] = ' '
    if 'total_gold' not in request.session:
        request.session['total_gold'] = 0
    return render(request, 'index.html', context)


def process_money(request):
    value = request.session['total_gold']
    if request.POST['find_gold'] == 'Farm':
        value = random.randint(10, 20)
        request.session['total_gold'] += value
        request.session['activities'] = f"{request.session['activities']} {value} gold was added"
    if request.POST['find_gold'] == 'Cave':
        value = random.randint(5, 10)
        request.session['total_gold'] += value
        request.session['activities'] = f"{request.session['activities']} {value} gold was added"
    if request.POST['find_gold'] == 'House':
        value = random.randint(2, 5)
        request.session['total_gold'] += value
        request.session['activities'] = f"{request.session['activities']} {value} gold was added"
    if request.POST['find_gold'] == 'Casino':
        value = random.randint(-50, 50)
        request.session['total_gold'] += value
        request.session['activities'] = f"{request.session['activities']} {value} gold was added"
    return redirect('/')

def reset(request):
    del request.session['activities']
    del request.session['total_gold']
    return redirect('/')