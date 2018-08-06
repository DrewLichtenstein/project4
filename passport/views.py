from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse
import json
from . models import Your_Park, Park_Review, Friend

#index is the default Django singup page
def index(request):
    return HttpResponseRedirect(reverse("signup"))

#registration page
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(reverse("your_passport"))
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

#login authentication
def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("your_passport"))
    else:
        return render(request, "login.html", {"message": "Invalid credentials."})

#logout
def login_redirect(request):
    return render(request, "login.html")


#logout function
def logout_view(request):
    logout(request)
    return render(request, "login.html", {"message": "Logged out."})

# initial information needed to render the passport page: park names, reviews, list of users, and list of this
# user's friends and previously saved parks.
def your_passport(request):
    storage = messages.get_messages(request)
    username = request.user
    with open('passport/park_data.json') as json_data:
        d = json.load(json_data)
        park_names = []
        for park in d["data"]:
            park_names.append(park["fullName"])
        context = {
            "park_names": park_names,
            "your_park": Your_Park.objects.filter(username=username).all(),
            "park_reviews": Park_Review.objects.all(),
            "users": User.objects.all(),
            "friends": Friend.objects.filter(username=username).all(),
            "username": username,
            "message": storage
        }
    return render(request,'your_passport.html', context)

# when a user selects a park, it saves as a Your_Park class and reloads the page
def add_park_information(request):
    username = request.user
    selected_park = request.POST["selected_park"]
    with open('passport/park_data.json') as json_data:
        d = json.load(json_data)
        for park in d["data"]:
            if park["fullName"] == selected_park:
                park_description = (park["description"])
    your_park_list = Your_Park.objects.filter(username=username).all()
    for x in your_park_list:
        if x.park_name == selected_park:
            messages.error(request, 'Park already in your profile!')
            return redirect(reverse("your_passport"))
    f = Your_Park(username=username, park_name=selected_park, park_description=park_description)
    f.save()
    return redirect(reverse("your_passport"))

# when a user submits a review, it saves it as a Park_Review class and reloads the page
def submit_review(request):
    username = request.user
    park_name = request.POST["park_name"]
    review = str(request.POST["form_review"])
    f = Park_Review(username=username, park_name=park_name, review=review)
    f.save()
    return HttpResponseRedirect(reverse("your_passport"))

# when adds a friend, it saves it as a Friends class and reloads the page
def add_friend(request):
    username = request.user
    friend = request.POST["users_not_yet_friend"]
    friend_list = Friend.objects.filter(username=username).all()
    for x in friend_list:
        if x.friend == friend:
            return HttpResponseRedirect(reverse("your_passport"))
    f = Friend(username=username, friend=friend)
    f.save()
    return HttpResponseRedirect(reverse("your_passport"))

def remove_from_passport(request):
    entry_id = request.POST["entry_id"]
    park_to_remove = Your_Park.objects.get(pk=entry_id)
    park_to_remove.delete()
    return HttpResponseRedirect(reverse("your_passport"))