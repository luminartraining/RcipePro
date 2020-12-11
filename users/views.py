from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
# Create your views here.
from users.models import Profile
from .forms import UserRegistrationForm,LoginForm,ProfileCreateForm
from recipes.models import Recipe
def register(request):
    form=UserRegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signIn")
    return render(request,"users/registration.html",context)



def signIn(request):


    if request.method=="POST":


        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)

            return redirect("home")
        else:

            return render(request, "users/userlogin.html")
    return render(request,"users/userlogin.html")


def home(request):
    context={}
    recipes=Recipe.objects.all()
    context["recipes"]=recipes
    return render(request, "users/userhome.html",context)

def singOut(request):
    logout(request)
    return redirect("signIn")



def create_profile(request):
    form=ProfileCreateForm(initial={"user":request.user})
    context={}
    context["form"]=form
    if request.method=="POST":
        form=ProfileCreateForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")

        else:
            context["form"]=form
            return render(request, "users/createprofile.html", context)
    return render(request,"users/createprofile.html",context)


def edit_profile(request):
    user=Profile.objects.get(user=request.user)
    form=ProfileCreateForm(initial={"user":request.user},instance=user)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=ProfileCreateForm(instance=user,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            context["form"]=form
            return render(request, "users/editprofile.html", context)

    return render(request,"users/editprofile.html",context)



def view_profile(request):
    user = Profile.objects.get(user=request.user)
    context={}
    context["users"]=user
    return render(request,"users/viewprofile.html",context)






