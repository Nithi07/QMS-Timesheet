from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from QMS.models import Auditschedule
from QMS.models import EmployeeDetails
from QMS.models import Audittype
from QMS.models import WorkManual
from QMS.models import ManualCheckList
from QMS.models import Audit_comments
from QMS.models import Postpond
from QMS.models import AuditscheduleConfirm
from QMS.form.auditscheduleform import Auditscheduleform
from QMS.form.auditscheduleform import Postpondform
from QMS.form.auditscheduleform import Cancelform
from QMS.form.auditscheduleform import Confirmform
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView,View
from django.urls import  reverse_lazy
from django.contrib import messages


# Auditschedule ListView
class AuditscheduleListview(ListView):
    model = Auditschedule
    template_name = 'superadmin/auditshedule_view.html'
    def get_context_data(self, **kwargs):
        auditcomments = Audit_comments.objects.all()
        aud_id = [i.auditschedule_id for i in auditcomments if str(i.auditee_status) != "Completed" ]
        aud_typ = [i.auditschedule_id for i in auditcomments if str(i.auditee_status) != "Completed" or str(i.auditee_comments) == "None"]
        aud_typ_all = [i.auditschedule_id for i in auditcomments]
        verify = [i.auditschedule_id for i in auditcomments if str(i.verified_status) != 'Verified']
        auditschedule = Auditschedule.objects.all().order_by('pk')
        obj = {'auditschedule':auditschedule,'auditcomments':aud_id,'aud_typ':aud_typ,'aud_typ_all':aud_typ_all,'verify':verify}
        return obj


class AuditscheduleConfirmListview(ListView):
    model = AuditscheduleConfirm
    form_class = Confirmform
    template_name = 'superadmin/auditschedule_confirm.html'
    success_url = 'QMS:auditscheduleview'

    def get_success_url(self):
        return reverse_lazy(self.success_url)

    def get_context_data(self):
        auditschedule = Auditschedule.objects.get(pk=self.kwargs['pk'])
        audcon = AuditscheduleConfirm.objects.all()
        approval = [i.auditee_name for i in audcon if str(auditschedule.id) == i.auditschedule_id]
        aude_lis=[o.emp_name for o in auditschedule.schedule_auditee_list.all()]
        print(approval)
        print(aude_lis)
        obj = {'auditschedule':auditschedule,'form':Confirmform(),
                'employeedetails':EmployeeDetails.objects.all(),
                'approval':approval,'aude_lis':aude_lis}
        return obj

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = Confirmform(request.POST or None)
            if form.is_valid():
                return self.form_valid(form,request)
            else:
                return self.form_invalid(form)

    def form_valid(self,form,request):
        a_name = request.POST.get('auditee_name')
        ash_id = request.POST.get('auditschedule_id')
        app = request.POST.get('approved_by')
        app_sts = request.POST.get('approved_status')
        instance = AuditscheduleConfirm.objects.create(auditee_name=a_name,auditschedule_id=ash_id,approved_by=app,
                                approved_status=app_sts)
        return HttpResponseRedirect(self.get_success_url())




class AuditscheduleConfirming(View):
    model = Auditschedule
    success_url = 'QMS:auditscheduleview'

    def get_success_url(self):
        return reverse_lazy(self.success_url)

    def get(self, request, *args, **kwargs):
        auditschedule = self.model.objects.get(pk=self.kwargs.get("pk"))
        Q1 = ['01','02','03']
        Q2 = ['04','05','06']
        Q3 = ['07','08','09']
        Q4 = ['10','11','12']
        ac = []
        # auditees = auditschedule.schedule_auditee_list.emp_name
        auditype = auditschedule.schedule_auditype.auditcode
        ad = auditschedule.schedule_audit_date
        auditdate = str(ad).split('-')
        ac.append(auditype)
        if auditdate[1] in Q1:
            ac.append('Q1')
        elif auditdate[1] in Q2:
            ac.append('Q2')
        elif auditdate[1] in Q3:
            ac.append('Q3')
        elif auditdate[1] in Q4:
            ac.append('Q4')
        ac.append(auditdate[0])
        ac.append(str(auditschedule.id))
        auditcode = '/'.join(ac)
        auditschedule.schedule_audit_code = auditcode
        auditschedule.save()
        return HttpResponseRedirect(self.get_success_url())




# Auditschedule CreateView
class AuditscheduleCreate(CreateView):
    model = Auditschedule
    form_class = Auditscheduleform
    success_url = 'QMS:auditscheduleview'
    template_name = 'superadmin/auditshedule_form.html'

    def get_context_data(self, **kwargs):
        context = super(AuditscheduleCreate, self).get_context_data(**kwargs)
        context["form"] = Auditscheduleform()
        return context

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            form = Auditscheduleform(request.POST or None)
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)
                # messages.error(request, 'The form is invalid')


    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
       return reverse_lazy(self.success_url)

class AuditscheduleUpdate(UpdateView):
     model = Auditschedule
     form_class = Auditscheduleform
     success_url = 'QMS:auditscheduleview'
     template_name = 'superadmin/auditshedule_form.html'

     def get_success_url(self):
        return reverse_lazy(self.success_url)

     def form_valid(self, form):
        form = self.get_form()
        form.save()
        return HttpResponseRedirect(self.get_success_url())


#Auditschedule DeleteView
class AuditscheduleDelete(DeleteView):
    model = Auditschedule
    success_url = 'QMS:auditscheduleview'
    template_name = 'superadmin/auditschedule_confirm_delete.html'
    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(AuditscheduleDelete, self).get_object()
        return obj

    def get_success_url(self):
        return reverse_lazy(self.success_url)


class AuditschedulePostpond(ListView):
    model = Postpond
    form_class = Postpondform
    success_url = 'QMS:auditscheduleview'
    template_name = 'superadmin/postpond_form.html'
    def get_context_data(self, **kwargs):
        aa = Postpond.objects.all()
        lis = [int(i.auditschedule_id) for i in aa]
        context = super(AuditschedulePostpond, self).get_context_data(**kwargs)
        context["auditschedule"] = Auditschedule.objects.get(pk=self.kwargs.get("pk"))
        context["postpond"] = lis
        context["form"] = Postpondform()

        return context

    def post(self, request, *args, **kwargs):
        form = Postpondform(request.POST)
        if form.is_valid():
            Auditschedule.objects.filter(pk=self.kwargs.get("pk")).update(
            schedule_audit_date= request.POST.get('post_date'),
            schedule_audit_time = request.POST.get('post_time'),
            )
            form.save()
            return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
       return reverse_lazy(self.success_url)


class AuditscheduleCancel(ListView):
    model = Auditschedule
    form_class = Cancelform
    template_name = 'superadmin/auditschedule_cancel.html'
    success_url = 'QMS:auditscheduleview'

    def get_context_data(self, **kwargs):
        context = super(AuditscheduleCancel, self).get_context_data(**kwargs)
        context["auditschedule"] = Auditschedule.objects.get(pk=self.kwargs.get("pk"))
        context["form"] = Cancelform()
        return context

    def post(self, request, *args, **kwargs):
        form = Cancelform(request.POST)
        if form.is_valid():
            Auditschedule.objects.filter(pk=self.kwargs.get("pk")).update(schedule_description = request.POST.get('schedule_description'),
            schedule_audit_status = '2'
            )
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
       return reverse_lazy(self.success_url)


def AuditscheduleClosed(request, id):#not mention id instead of pk in url
    Auditschedule.objects.filter(id=id).update(schedule_audit_status = '1')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
