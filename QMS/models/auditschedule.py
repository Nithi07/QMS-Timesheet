from django.db import models
from QMS.models import ListAuditors
from QMS.models import  Audittype
from QMS.models.employee_details import EmployeeDetails


class Auditschedule(models.Model):
    schedule_auditype=models.ForeignKey(Audittype,related_name='audit_type', on_delete=models.CASCADE)
    schedule_job_code = models.CharField(max_length=15,null=True)
    schedule_sub_job_code = models.CharField(max_length=15,blank=True,null=True)
    schedule_job_audit_no = models.CharField(max_length=15,blank=True,null=True)
    schedule_audit_no = models.CharField(max_length=50 ,blank=True,null=True)
    schedule_audit_code = models.CharField(max_length=50,blank=True,null=True)
    schedule_audit_date = models.DateField(null=True)
    schedule_audit_time = models.TimeField(null=True)
    schedule_auditee_list = models.ManyToManyField(EmployeeDetails, blank=True, related_name='auditee_list' )
    schedule_auditor_list = models.ManyToManyField(ListAuditors, blank=True, related_name='auditor_list' )
    schedule_department_status = models.IntegerField(default=0)
    schedule_department_username = models.CharField(max_length=15,blank=True,null=True)
    schedule_department_date = models.DateField(blank=True,null=True)
    schedule_final_auditor_list = models.ManyToManyField(ListAuditors, blank=True, related_name='final_auditor_list' )
    schedule_team_member_list = models.ManyToManyField(EmployeeDetails, blank=True, related_name='team_member_list' )
    schedule_audit_mr_status = models.IntegerField(default=0)
    schedule_description = models.CharField(max_length=15,blank=True,null=True)
    schedule_audit_status = models.IntegerField(default=0)
    schedule_file_path = models.URLField(max_length = 500,blank=True,null=True)
    schedule_iso_year = models.CharField(max_length = 50,null=True)
    create_by = models.CharField(max_length=50,null=True)
    create_on = models.DateTimeField(auto_now=True,null=True)
    create_ip = models. GenericIPAddressField(blank=True,null=True)
    modified_by = models.CharField(max_length=50,null=True)
    modified_on = models.DateTimeField(auto_now=True)
    modified_ip = models. GenericIPAddressField(blank=True,null=True)

    class Meta:
       db_table = 'audit_schedule'


class AuditscheduleConfirm(models.Model):
    auditschedule_id = models.CharField(max_length=4,null=True)
    auditee_name = models.CharField(max_length=50,null=True)
    auditee_department = models.CharField(max_length=50,null=True)
    approved_by = models.CharField(max_length=50,null=True)
    approved_status = models.CharField(max_length=50,null=True)

    class Meta:
       db_table = 'auditschedule_confirm'
