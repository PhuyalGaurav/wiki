from django.shortcuts import render, redirect
from markdown2 import Markdown
from . import util
from django.http import Http404
from random import choice
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)

markdowner = Markdown()


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
