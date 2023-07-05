from django.shortcuts import render
from markdown2 import Markdown
from . import util

markdowner = Markdown()


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entries(request, name):
    if name in util.list_entries():
        return render(request,'encyclopedia/entries.html',{
            "exist" : True,
            "name" : name,
            "markdown" : markdowner.convert(util.get_entry(name))
        })
    else:
        return render(request,'encyclopedia/entries.html',{
            "name" : name,
            "exist" : False,
        })
