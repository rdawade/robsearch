from django.forms import ModelForm, fields
from .models import Project,Review
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title','featured_image','descriptions','demo_link','source_link']
        widgets = {
            'tags':forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm,self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})

       # self.fields['title'].widget.attrs.update({'class':'input','placeholder':'Add title'})


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value','body']

        labels = {
        'value':'place your vote',
        'body':'Add a commdents with your name'
        }

    
    def __init__(self, *args, **kwargs):
        super(ReviewForm,self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'input'})