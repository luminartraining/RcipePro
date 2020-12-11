from django.shortcuts import render,redirect

# Create your views here.
from recipes.forms import CreateRecipeForm
from recipes.models import Recipe

def create_recipe(request):
    form=CreateRecipeForm(initial={"created_by":request.user})

    context={}
    context["form"]=form

    if request.method=="POST":
        form=CreateRecipeForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listmyrecipes")
        else:
            context["form"]=form
            return render(request, "recipes/createrecipe.html", context)

    return render(request,"recipes/createrecipe.html",context)

def list_my_recipes(request):
    my_recipes=Recipe.objects.filter(created_by=request.user)
    context={}
    context["recipes"]=my_recipes

    return render(request,"recipes/myRecipes.html",context)


def edit_recipe(request,id):
    recipe=Recipe.objects.get(id=id)
    form=CreateRecipeForm(instance=recipe)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=CreateRecipeForm(instance=recipe,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("listmyrecipes")
        else:
            context["form"]=form
            return render(request, "recipes/editrecipe.html", context)

    return render(request,"recipes/editrecipe.html",context)


def view_recipe(request,id):
    recipe = Recipe.objects.get(id=id)
    context={}
    context["recipe"]=recipe
    return render(request,"recipes/recipeview.html",context)

def delete_recipe(request,id):
    Recipe.objects.get(id=id).delete()
    return redirect("listmyrecipes")
