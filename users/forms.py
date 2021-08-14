from django.forms import ModelForm, fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,skill,Message

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','password1','password2']
        labels = {
            'first_name':'Name',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'}) 


class ProfileForm(ModelForm):
    class Meta:

        model = Profile
        fields = ['name','email','username','location','bio','short_intro',
        'profile_image','social_github','social_linkedin','social_youtube',
        'social_website','social_twitter']

    
    def __init__(self, *args, **kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'}) 


class SkillForm(ModelForm):
    class Meta:
        model = skill
        fields = '__all__'
        exclude = ['owner']


    def __init__(self, *args, **kwargs):
        super(SkillForm,self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'}) 


class MesssageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name','email','subject','body']

        
    def __init__(self, *args, **kwargs):
        super(MesssageForm,self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'}) 
