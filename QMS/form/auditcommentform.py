from django import forms
from QMS.models import Auditschedule
from QMS.models import ListAuditors
from QMS.models import Audittype
from QMS.models import EmployeeDetails
from QMS.models import Audit_comments
from QMS.models import ManualCheckList
from QMS.models import EmployeDepartment
from django.urls import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab,FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset,Reset,Button,HTML,ButtonHolder


class Auditor_commentsForm(forms.ModelForm):
    audittype = forms.CharField(max_length=25)
    cls_refno = forms.CharField(max_length=8)
    description = forms.CharField(max_length=100)
    auditor_status = forms.CharField(max_length=10,required=True)
    department = forms.CharField(max_length=10,required=True)
    auditschedule_id = forms.IntegerField()
    workmanual_id = forms.IntegerField()
    auditor_comments = forms.CharField(
            widget = forms.Textarea(attrs={'rows': 3, 'cols': 50}),
            required = True
            )

    class Meta:
        model = Audit_comments
        fields = ['audittype','cls_refno','description','auditor_comments','auditor_status','department','auditschedule_id','workmanual_id']




class Auditee_commentsForm(forms.ModelForm):
    auditee_status = forms.CharField(max_length=15)
    class Meta:
        model = Audit_comments
        fields = ['auditee_comments','auditee_status',]

        widgets = {
            'auditee_comments': forms.Textarea(attrs={'rows': 2, 'cols': 22}),
        }


class Verified_commentsForm(forms.ModelForm):

    verified_status = forms.CharField(max_length=10)

    class Meta:
        model = Audit_comments
        fields = ['verified_comments','verified_status',]

        widgets = {
            'verified_comments': forms.Textarea(attrs={'rows': 2, 'cols': 22}),
        }

class mr_commentsForm(forms.ModelForm):
    mr_status = forms.CharField(max_length=10)
    class Meta:
        model = Audit_comments
        fields = ['mr_comments','mr_status',]
        widgets = {
            'mr_comments': forms.Textarea(attrs={'rows': 2, 'cols': 22}),
        }
