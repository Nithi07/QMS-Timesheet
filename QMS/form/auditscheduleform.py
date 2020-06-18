from django import forms
from QMS.models import Auditschedule
from QMS.models import ListAuditors
from QMS.models import Audittype
from QMS.models import EmployeeDetails
from QMS.models import Audit_comments
from QMS.models import ManualCheckList
from QMS.models import EmployeDepartment
from QMS.models import WorkManual
from QMS.models import Postpond
from QMS.models import AuditscheduleConfirm
from django.urls import reverse
from crispy_forms.bootstrap import Field, InlineRadios, TabHolder, Tab,FormActions
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset,Reset,Button,HTML,ButtonHolder



class Auditscheduleform(forms.ModelForm):
    schedule_auditype = forms.ModelChoiceField(
                        queryset=Audittype.objects.all(),
                        label = 'Audit Type',
                        empty_label = 'Select',required=True)
    schedule_auditor_list = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(),queryset=ListAuditors.objects.all(),label = 'Auditor List',required=True)
    schedule_auditee_list = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(),queryset=EmployeeDetails.objects.all(),label = 'Auditee List',required=True)
    schedule_job_code = forms.CharField(max_length=15,label = 'Job Code')
    schedule_sub_job_code = forms.CharField(max_length=15,label = 'Sub JobCode')
    schedule_audit_date = forms.DateField(label = 'Audit Date',required=True,widget=forms.TextInput(
                                    attrs={'type':'date'}
                                    ))
    schedule_audit_time = forms.TimeField(label = 'Audit Time',required=True,widget=forms.TextInput(
                                    attrs={'type':'time'}
                                    ))
    schedule_iso_year = forms.ModelChoiceField(
                        queryset=WorkManual.objects.all(),
                        label = 'ISO Year',
                        empty_label = 'Select',required=True)
    schedule_final_auditor_list  = forms.ModelMultipleChoiceField(widget=forms.CheckboxSelectMultiple(),queryset=ListAuditors.objects.all(),label = 'Final Auditor List',required=True)

    def __init__(self, *args, **kwargs):
        super(Auditscheduleform, self).__init__(*args, **kwargs)
        self.fields['schedule_auditype'].label_from_instance = lambda obj: "%s" % obj.audittype
        self.fields['schedule_auditype'].widget.attrs['style'] = 'height:40px;'
        self.fields['schedule_auditor_list'].label_from_instance = lambda obj: "%s" % obj.auditors.emp_name
        self.fields['schedule_auditee_list'].label_from_instance = lambda obj: "%s" % obj.emp_name
        self.fields['schedule_final_auditor_list'].label_from_instance = lambda obj: "%s" % obj.auditors.emp_name
        self.fields['schedule_iso_year'].label_from_instance = lambda obj: "%s" % obj.ISO_certification_year
        self.fields['schedule_iso_year'].widget.attrs['style'] = 'height:40px;'
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.layout = Layout(Field(
            'schedule_auditype',
            'schedule_job_code',
            'schedule_sub_job_code',
            'schedule_audit_date',
            'schedule_audit_time',
            'schedule_auditee_list',
            'schedule_auditor_list',
            'schedule_iso_year',
            'schedule_final_auditor_list'),
            )

    class Meta:
        model = Auditschedule
        fields = ['schedule_auditype','schedule_job_code','schedule_sub_job_code','schedule_audit_date','schedule_audit_time',
                  'schedule_auditee_list','schedule_auditor_list','schedule_iso_year','schedule_final_auditor_list']


class Confirmform(forms.ModelForm):
    auditschedule_id = forms.CharField(max_length=4,required=False)
    auditee_name = forms.CharField(max_length=50,required=False)
    approved_by = forms.CharField(max_length=50,required=False)
    approved_status = forms.CharField(max_length=50,required=False)

    class Meta:
        model = AuditscheduleConfirm
        fields = ['auditschedule_id','auditee_name','approved_by','approved_status']


class Postpondform(forms.ModelForm):
    post_date = forms.DateField()
    post_time = forms.TimeField()
    auditschedule_id = forms.CharField(max_length=5)

    class Meta:
        model = Postpond
        fields = ['post_date','post_time','reason','auditschedule_id']
        widgets = {
            'reason': forms.Textarea(attrs={'rows': 2, 'cols': 22}),
        }

class Cancelform(forms.ModelForm):

    class Meta:
        model = Auditschedule
        fields = ['schedule_description']
        widgets = {
            'schedule_description': forms.Textarea(attrs={'rows': 2, 'cols': 22}),
        }
