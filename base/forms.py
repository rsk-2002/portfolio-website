from django.forms import ModelForm
from .models import Project, Message, Skill, Endorsement, Comment


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'thumbnail', 'body']


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        exclude = ['id', 'is_read']

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'
        exclude = ['id']

class EndorsementForm(ModelForm):
    class Meta:
        model = Endorsement
        fields = ['name', 'body']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'body']