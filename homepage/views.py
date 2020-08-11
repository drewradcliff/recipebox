from django.shortcuts import render, HttpResponseRedirect, reverse

from homepage.models import Recipe, Author
from homepage.forms import AddRecipeForm, AddAuthorForm

# Create your views here.


def index(request):
    recipes = Recipe.objects.all()
    return render(request, "index.html", {"recipes": recipes})


def recipe(request, recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, "recipe.html", {"recipe": recipe})


def author(request, author_id):
    author = Author.objects.filter(id=author_id).first()
    author_recipes = Recipe.objects.filter(author=author_id)
    return render(request, "author.html", {"author": author, "author_recipes": author_recipes})


def add_author(request):
    if request.method == "POST":
        form = AddAuthorForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))

    form = AddAuthorForm()
    return render(request, "generic_form.html", {"form": form})


def add_recipe(request):
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))

    form = AddRecipeForm()
    return render(request, "generic_form.html", {"form": form})
