from django import forms
from app.models import *
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
        #fields=['Topic_name']
        #exclude=['Topic_name']
        

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields='__all__'
        #fields=['Name','Url','Email']
        #exclude=['Email','Url']
        #widgets={'Name':forms.PasswordInput}
        #help_text={'Url':'should not be integers','Name':'should be Capita Letters'}

class AccessForm(forms.ModelForm):
    class Meta:
        model=AccessRecord
        fields='__all__'
       # fields=['Name','Author']
        #exclude=['Name','Author']
        #widgets={'Author':forms.Textarea(),'Date':forms.PasswordInput}
        #labels={'Name':'N','Author':'AU','Date':'Dt'}