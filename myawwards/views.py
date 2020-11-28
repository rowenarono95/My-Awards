from django.shortcuts import render

# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    project= Project.all_projects()
    json_projects = []
    for project in project: