from django import forms
from .models import Partne, Projects, Program

class partnerform(forms.ModelForm):
    class Meta:
        model = Partne
        fields = ('firstname', 'lastname','email', 'address', 'interest', 'biodata', 'acceptancenote')

class projectform(forms.ModelForm):
    class Meta:
        model = Projects
        fields =('name', 'description','employess','pam','tasks','objcetives','program','startdate','endperiod')
        #'__all__'name
   # def __init__(self, *args, **kwargs):
   #     super(projectform, self).__init__(*args, **kwargs)
   #     self.fields['startdate'].disabled = True       
        
class programform(forms.ModelForm):
    class Meta:
        model = Program
        fields = ('name','districts', 'employees', 'project')        