from asyncio.log import logger
from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.models import User

import logging, traceback

logger = logging.getLogger('django')

# Create your views here.

def index(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        #password2 = request.POST['password2']
        email = request.POST['email']

        user = User.objects.create_user(username=username,first_name=first_name, last_name=last_name, password=password1, email=email)
        user.save()
        return render(request, 'register1.html')
    else:
        print("Registration page")
        logger.info("Rgistration page, fill the details")
        return render(request, 'register.html')

def register1(request):
    print("User Is Register")
    logger.info('user is registered')
    return HttpResponse(render(request, 'register1.html'))


def addUser(request):
    val = {'response': 'User Added'}
    print("Hello addUser")
    logger.info("User is added")
    return JsonResponse(val, status=200)

def addSomething(request):
    val = {'response': "Something Added"}
    print("Add Something")
    logger.warning("Something warning wrong")
    return JsonResponse(val, status=200)

def addNew(request, someNumber):
    val = {'response': "Something Added New", "numberGiven":int(someNumber)}
    print("Add New")
    if int(someNumber) > 50:
        val1 = {'response': "Number is > 50", "numberGiven":int(someNumber)}
        logger.info("Number must be less than(<) 50")
        return JsonResponse(val, status=500)
    else:
        logger.info("Something info wrong")
        return JsonResponse(val, status=200)

def addNewError(request, someNumber):
    val = {"response" : "Something Added New", "numberGiven":someNumber}
    print("Add Error")
    try:
        if int(someNumber) > 50:
            logger.error("something error wrong")
            return JsonResponse(val, status=500)
        else:
            logger.info("something info wrong")
            return JsonResponse(val, status=200)
    
    except Exception as e:
        print(str(e))
