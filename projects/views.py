from django.shortcuts import render, get_object_or_404, redirect
from projects.models import Project
from projects.forms import ProjectForm
from django.contrib.auth.decorators import login_required
from tasks.models import Task

# Create your views here.
@login_required
def list_projects(request):
    projects = Project.objects.filter(owner=request.user)
    context = {"projects": projects}
    return render(request, "projects/list.html", context)


@login_required
def show_project(request, id):
    projects = get_object_or_404(Project, id=id)
    tasklist = Task.objects.filter(assignee=request.user)
    context = {"project_object": projects, "tasklist_object": tasklist}
    return render(request, "projects/detail.html", context)


@login_required
def create_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            project = form.save(False)
            project.owner = request.user
            project.save()
            return redirect("list_projects")
    else:
        form = ProjectForm()
        context = {
            "form": form,
        }
    return render(request, "projects/create.html", context)
