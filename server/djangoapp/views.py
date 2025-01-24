from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout, login, authenticate
from .models import CarMake, CarModel
from django.contrib import messages
from datetime import datetime
import logging
import json

from django.views.decorators.csrf import csrf_exempt
# from .populate import initiate

# Get an instance of a logger
logger = logging.getLogger(__name__)

# Create your views here.

# Create a `login_user` view to handle sign-in request
@csrf_exempt
def login_user(request):
    # Get username and password from request.POST dictionary
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']
    # Try to check if provided credentials can be authenticated
    user = authenticate(username=username, password=password)
    data = {"userName": username}
    if user is not None:
        # If user is valid, call login method to log in the current user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}
    else:
        data = {"userName": username, "status": "Authentication Failed"}
    return JsonResponse(data)

# Create a `logout_request` view to handle sign-out request
@csrf_exempt
def logout_request(request):
    # Log out the current user
    logout(request)
    # Return a JSON response with an empty username
    data = {"userName": ""}
    return JsonResponse(data)
# Method to get the list of cars
def get_cars(request):
    count = CarMake.objects.filter().count()
    print(count) # Debugging prints the count of CarMake objects
    car_models = CarModel.objects.select_related('car_make') # optimized query to fetch related CarMake
    cars = []
    for car_model in car_models:
        cars.append({"CarModel": car_model.name, "CarMake": car_model.car_make.name})   
    return JsonResponse({"CarModels": cars})
        
        
 # Create a `registration` view to handle sign-up request
# @csrf_exempt
# def registration(request):
#     ...

# Update the `get_dealerships` view to render the index page with
# a list of dealerships
# def get_dealerships(request):
#     ...

# Create a `get_dealer_reviews` view to render the reviews of a dealer
# def get_dealer_reviews(request, dealer_id):
#     ...

# Create a `get_dealer_details` view to render the dealer details
# def get_dealer_details(request, dealer_id):
#     ...

# Create a `add_review` view to submit a review
# def add_review(request):
#     ...
