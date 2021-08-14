from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from .models import Project,Tag
from .forms import ProjectForm,ReviewForm   
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .utils import searchProjects,paginateProjects
from django.contrib import messages





def function(request):
    proje,search_query = searchProjects(request)
    custom_range , projects  = paginateProjects(request,proje,6)
    

    context={'proje':projects , 'search_query':search_query , 'custom_range':custom_range}
    return render(request,'projects/projects.html',context)

def projec(request,pk):
    projectObj = Project.objects.get(id=pk)
    form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.project = projectObj
        review.owner = request.user.profile
        review.save()

        projectObj.getVoteCount
        messages.success(request,'Your review was succesfully submited!')
        return redirect('pro' ,pk = projectObj.id)

        
    return render(request,'projects/single-project.html',{'project':projectObj,'form':form})


@login_required(login_url= "login")
def createproject(request):
    profile = request.user.profile
    form = ProjectForm()

    if request.method == "POST":
        newtags = request.POST.get('newtags').replace(',', " ").split()
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project =  form.save(commit=False)
            project.owner = profile
            project.save()
            
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)
            return redirect('projects')
    context = {'form':form}
    return render(request,"projects/project_form.html",context)


@login_required(login_url= "login")
def updateproject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        newtags = request.POST.get('newtags').replace(',', " ").split()
        

        form = ProjectForm(request.POST,request.FILES,instance=project)

        if form.is_valid():
            project = form.save()
            for tag in newtags:
                tag, created = Tag.objects.get_or_create(name=tag)
                project.tags.add(tag)

            return redirect('projects')
    context = {'form':form, 'project':project}
    return render(request,"projects/project_form.html",context)


@login_required(login_url= "login")
def deleteproject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST':
        project.delete()
        return redirect('account')
    context = {'object':project}
    return render(request,'delete_template.html',context)


