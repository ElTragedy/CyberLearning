import json
from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse, HttpResponseForbidden
from functools import wraps


def render_module(request):
    role = request.session.get("role")  # No default value
    if not role:
        return redirect("select_role")  # Redirect to role selection if no role is set
    
    try:
        with open("data/test.json") as f:
            data = json.load(f)
    except FileNotFoundError:
        raise Http404("JSON file not found.")
    
    return render(request, "module.html", {"module": data["module"], "role": role})

    
    # Pass the data to the template
    return render(request, "module.html", {"module": data["module"]})

def home(request):
    return render(request, "home.html")

def edit_json(request):
    # Define the path to the JSON file
    json_file_path = "data/test.json"
    
    if request.method == "POST":
        # Handle saving the edited JSON
        try:
            new_data = json.loads(request.POST.get("json_content"))  # Parse JSON from form input
            with open(json_file_path, "w") as f:
                json.dump(new_data, f, indent=4)  # Save updated JSON back to file
            return redirect("render_module")  # Redirect back to the module view
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON data. Please fix any syntax errors.", status=400)
    
    # Load the JSON file for rendering
    try:
        with open(json_file_path) as f:
            data = json.load(f)
    except FileNotFoundError:
        raise Http404("JSON file not found.")
    
    return render(request, "edit_json.html", {"json_content": json.dumps(data, indent=4), "module": data["module"]})


# Role selection view
def select_role(request):
    return render(request, "select_role.html")

def set_role(request, role):
    if role in ["student", "teacher", "admin"]:
        request.session["role"] = role
        request.session.modified = True  # Explicitly mark the session as modified
        return redirect("home")
    else:
        return HttpResponse("Invalid role", status=400)


# Home view
def home(request):
    role = request.session.get("role", "guest")  # Default role is "guest"
    return render(request, "home.html", {"role": role})


def role_required(required_role):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            role = request.session.get("role", "guest")
            if role != required_role:
                return render(request, "403.html", status=403)
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

# Example student-specific view
@role_required("student")
def student_view(request):
    # Only accessible to users in the "student" role
    return render(request, "student_view.html", {"role": "student"})

@role_required("teacher")
def teacher_view(request):
    # Only accessible to users in the "teacher" role
    return render(request, "teacher_view.html", {"role": "teacher"})

@role_required("admin")
def admin_view(request):
    # Only accessible to users in the "admin" role
    return render(request, "admin_view.html", {"role": "admin"})

