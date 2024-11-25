import json
from django.shortcuts import render
from django.http import Http404

def render_module(request):
    try:
        # Load JSON from file
        with open("data/test.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise Http404("JSON file not found.")
    
    # Pass the data to the template
    return render(request, "module.html", {"module": data["module"]})

def home(request):
    return render(request, "home.html")