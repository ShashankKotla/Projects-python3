from django.shortcuts import render
from projects.models import Project

# Create your views here.
def project_index(request):
    project_indexs = Project.objects.all()
    context = {
        "project_indexs" : project_indexs
    }
    return render(request, "projects/project_index.html", context)

def project_detail(request, pk):
    project_details= Project.objects.get(pk=pk)
    context = {
        'project_details':project_details
    }
    return render(request, "projects/project_details.html", context)