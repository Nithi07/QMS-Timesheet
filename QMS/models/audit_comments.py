from django.db import models
from QMS.models import Audittype
from QMS.models import ManualCheckList
from QMS.models import EmployeDepartment

class Audit_comments(models.Model):

    workmanual_id = models.IntegerField(null=True)
    auditschedule_id = models.IntegerField(null=True)
    audittype = models.CharField(max_length=25,null=True)
    cls_refno = models.CharField(max_length=8,null=True)
    description = models.CharField(max_length=100,null=True)
    auditor_comments = models.TextField(null=True)
    auditor_status = models.CharField(max_length=10,null=True)
    department = models.CharField(max_length=25,null=True)
    auditee_comments = models.TextField(null=True)
    auditee_status = models.CharField(max_length=15,null=True)
    verified_comments = models.TextField(null=True)
    verified_status = models.CharField(max_length=10,null=True)
    mr_comments = models.TextField(null=True)
    mr_status = models.CharField(max_length=10,null=True)
    create_by = models.CharField(max_length=50,null=True)
    create_on = models.DateTimeField(auto_now=True)
    create_ip = models.GenericIPAddressField(null=True)
    modified_by = models.CharField(max_length=50,null=True)
    modified_on = models.DateTimeField(auto_now=True)
    modified_ip = models.GenericIPAddressField(null=True)

    class Meta:
        db_table = 'audit_comments'
