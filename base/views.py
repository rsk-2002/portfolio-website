from django.shortcuts import render, redirect
from .models import Project, Skill, Message, Endorsement, Comment
from .forms import ProjectForm, MessageForm, SkillForm, EndorsementForm, CommentForm
from django.contrib import messages

# Create your views here.
def homePage(request):
    projects = Project.objects.all()
    detailedSkills = Skill.objects.exclude(body="")
    skills = Skill.objects.filter(body="")
    endorsement = Endorsement.objects.filter(approve=True)

    form = MessageForm()

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message was successfully sent.")

    context = {"projects": projects, "detailedSkills": detailedSkills, "skills": skills, "form": form, "endorsement":endorsement}
    return render(request, 'base/home.html', context)


def projectPage(request, pk):
    project = Project.objects.get(id=pk)
    count = project.comment_set.count()
    comments = project.comment_set.all().order_by('-created')

    form = CommentForm()

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.project = project
            comment.save()
            messages.success(request, "Your comment was successfully added.")



    context = {"project": project, "count": count, "comments": comments, "form": form}
    return render(request, 'base/project.html', context)


def addProject(request):
    form = ProjectForm()

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {"form": form}
    return render(request, 'base/project_form.html', context)


def editProject(request, pk):
    project = Project.objects.get(id=pk)
    form = ProjectForm(instance=project)

    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {"form": form}
    return render(request, 'base/project_form.html', context)


def inboxPage(request):
    inbox = Message.objects.all().order_by('is_read')
    unreadCount = Message.objects.filter(is_read=False).count()

    return render(request, 'base/inbox.html', {"inbox":inbox, "unreadCount": unreadCount})

def messagePage(request, pk):
    message = Message.objects.get(id=pk)
    message.is_read = True
    message.save()
    return render(request, 'base/message.html', {"message":message})



def addSkill(request):
    form = SkillForm()

    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill added successfully.")
            return redirect('home')

    return render(request, 'base/skills_form.html', {"form":form})


def addEndorsement(request):
    form = EndorsementForm()

    if request.method == "POST":
        form = EndorsementForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Thank you, Your endorsement added successfully.")
            return redirect('home')

    return render(request, 'base/endorsement_form.html', {"form":form})


def donationPage(request):

    return render(request, 'base/donation.html', {})