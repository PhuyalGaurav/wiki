from django.shortcuts import render, redirect
from markdown2 import Markdown
from . import util
from django.http import Http404
from random import choice
from django import forms
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt



markdowner = Markdown()

def error(request, code):
    return render(request, "encyclopedia/error.html", {
        "error" : code
    })

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entries(request, name):
    if name in util.list_entries():
        return render(request, 'encyclopedia/entries.html', {
            "exist": True,
            "name": name,
            "markdown": markdowner.convert(util.get_entry(name))
        })
    else:
        return render(request, 'encyclopedia/entries.html', {
            "name": name,
            "exist": False,
        })


def random(request):
    page = choice(util.list_entries())
    return entries(request, page)


def search(request):
    query = request.GET.get("q", "")
    if query is None or query == "":
        return render(request, "encyclopedia/search.html",{
        "found" : False ,
        "query" : query
    })

    antries = util.list_entries()

    results = [
        valid_entry
        for valid_entry in antries
        if query.lower() in valid_entry.lower()
    ]
    if len(results) == 1:
        return entries(request, results[0])

    return render(request, "encyclopedia/search.html",{
        "results" : results,
        "query" : query
    })

@csrf_exempt
def create(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        a= []
        for i in util.list_entries():
            a.append(i.lower())
        if title == "":
            return error(request, "Enter a title")
        elif title.lower() in a:
            return error(request, "Title Already Exists")
        elif content =="":
            return error(request, "Enter The Content")
        util.save_entry(title, content)
        return entries(request, title)
        

    if request.method == "GET":
        return render(request, "encyclopedia/create.html")
