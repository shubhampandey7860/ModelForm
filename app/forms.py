from django import forms
from app.models import *
#
class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic 
        fields = '__all__'
        
# Webpage        
class WebpageForm(forms.ModelForm):
    class Meta:
        model = Webpage 
        fields = '__all__' 
      # labels= {'topic_name':'tn','name':'na'}
      #  widgets = {'url':forms.PasswordInput}
       #  help_texts = {'name':'it contains only alphabets'}
        
# AccessRecord        
class AccessRecordForm(forms.ModelForm):
    class Meta:
        model = AccessRecord
        fields = '__all__'  
                     
