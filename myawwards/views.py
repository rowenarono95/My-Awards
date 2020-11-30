from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import  UserUpdateForm, ProfileUpdateForm, SignUpForm,RegistrationForm,profileForm,NewProjectForm
from .models import Profile,Project

# Create your views here.

@login_required(login_url='/accounts/login/')
def home(request):
    projects= Project.objects.all()
    return render(request,'index.html',{"projects":projects})
        
    
def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        procForm=profileForm(request.POST, request.FILES)
        if form.is_valid() and procForm.is_valid():
            username=form.cleaned_data.get('username')
            user=form.save()
            profile=procForm.save(commit=False)
            profile.user=user
            profile.save()
            # messages.success(request, f'Successfully created Account!.You can now login as {username}!')
        return redirect('login')
    else:
        form= RegistrationForm()
        prof=profileForm()
    params={
        'form':form,
        'profForm': prof
    }
    return render(request, 'users/register.html', params)


@login_required(login_url='/accounts/login/')
def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,f'Your account has been updated successfully!')
            return redirect('profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'profile.html', context)


def search_results(request):
    if 'project' in request.GET and request.GET['project']:
        search_term =request.GET.get('project')
        searched_project = Project.search_by_title(search_term)
        message = f'{search_term}'

        return render(request, 'search.html',{"message":message,"projects":searched_project})

    else:
        message = "You haven't searched for any term"

        return render(request,'search.html',{'message':message})


@login_required(login_url='/accounts/login/')   
def new_project(request):
    current_user = request.user
    user_profile = Profile.objects.get(user = current_user)
    if request.method == 'POST':
        form = NewProjectForm(request.POST,request.FILES)
        if form.is_valid:
            project_new = form.save(commit = False)
            project_new.user = user_profile
            project_new.save()
        return redirect('home')  
    else:
        form = NewProjectForm()
    return render(request,'new_project.html',{'form':form})

