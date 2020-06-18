from django.shortcuts import render, redirect
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from QMS.models import Auditschedule
from QMS.models import Audittype
from QMS.models import WorkManual
from QMS.models import ManualCheckList
from QMS.models import Audit_comments
from QMS.form.auditcommentform import Auditor_commentsForm,mr_commentsForm,Auditee_commentsForm,Verified_commentsForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import  reverse_lazy
from django.contrib import messages


class MrcommentListCreate(ListView):
    model = Audit_comments
    form_class = mr_commentsForm
    template_name = 'superadmin/auditorcomment_view.html'
    success_url = 'QMS:auditscheduleview'

    def get_context_data(self, **kwargs):
        context = super(MrcommentListCreate, self).get_context_data(**kwargs)
        context['form'] = mr_commentsForm()
        context["auditorcomments"] = Audit_comments.objects.filter(auditschedule_id=self.kwargs.get("pk")).order_by('pk')
        context["auditschedule"] = Auditschedule.objects.get(pk=self.kwargs.get("pk"))
        return context

    def post(self, request, *args, **kwargs):
        form = mr_commentsForm(request.POST)
        if form.is_valid():
            id = request.POST.getlist('id')
            mr_com = request.POST.getlist('mr_comments')
            mr_sts = request.POST.getlist('mr_status')
            c = len(id)
            for k in range(c):
                if mr_sts[k] != 'Accepted':
                    Audit_comments.objects.filter(pk=id[k]).update(mr_comments = mr_com[k],mr_status = mr_sts[k],verified_status='Re-submit')
                else:
                    Audit_comments.objects.filter(pk=id[k]).update(mr_comments = mr_com[k],mr_status = mr_sts[k])
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
       return reverse_lazy(self.success_url)


class MrcommentListUpdate(UpdateView):
     model = Audit_comments
     form_class = mr_commentsForm
     success_url = 'QMS:auditorcommentview'
     template_name = 'superadmin/mrcommet_update.html'

     def get_context_data(self, **kwargs):
             context = super(MrcommentListUpdate, self).get_context_data(**kwargs)
             context["auditcomments"] = Audit_comments.objects.get(pk=self.kwargs.get("pk"))
             return context

     def post(self, request, *args, **kwargs):
         form = mr_commentsForm(request.POST)
         if form.is_valid():
             Audit_comments.objects.filter(pk=self.kwargs.get("pk")).update(
             mr_comments = request.POST.get('mr_comments'),
             mr_status = request.POST.get('mr_status'),
             )
         return HttpResponseRedirect(self.get_success_url())

     def get_success_url(self):
        return reverse_lazy(self.success_url)



class AuditorcommentCreate(CreateView):
    model = Audit_comments
    form_class = Auditor_commentsForm
    template_name = 'superadmin/auditorcomment_form.html'
    success_url = 'QMS:auditscheduleview'

    def get_context_data(self, **kwargs):
        ashle = Auditschedule.objects.get(pk=self.kwargs.get("pk"))
        ac = Audit_comments.objects.all()
        wkm = []
        for i in WorkManual.objects.all():
            for j in i.audit_typ.all():
                if j.audittype == ashle.schedule_auditype.audittype:
                    wkm.append(i)
        context = super(AuditorcommentCreate, self).get_context_data(**kwargs)
        context["auditschedule"] = ashle
        context["workmanual"] = wkm
        context["form"] = Auditor_commentsForm()
        context['atype'] = [i.audittype for i in Audit_comments.objects.all()]
        return context

    def post(self, request, *args, **kwargs):
        model = Audit_comments()
        form = Auditor_commentsForm(request.POST)
        if  form.is_valid():
            a_type = request.POST.getlist('audittype')
            cls_no = request.POST.getlist('cls_refno')
            desc = request.POST.getlist('description')
            aud_cmt = request.POST.getlist('auditor_comments')
            aud_sts = request.POST.getlist('auditor_status')
            dept = request.POST.getlist('department')
            id = request.POST.getlist('auditschedule_id')
            wm_id = request.POST.getlist('workmanual_id')
            c = len(id) #take any variable lenth inside if condition
            for i in range(c):
                instance = Audit_comments.objects.create(audittype=a_type[i],cls_refno=cls_no[i],description=desc[i],
                                    auditor_comments=aud_cmt[i],auditor_status=aud_sts[i],department=dept[i],
                                    auditschedule_id = id[i],workmanual_id=wm_id[i])
        else:
            messages.error(request,"Failed")
        return HttpResponseRedirect(self.get_success_url())


    def get_success_url(self):
       return reverse_lazy(self.success_url)

#
# class Auditorcommentaddnew(CreateView):
#     model = Audit_comments
#     form_class = Auditor_commentsForm
#     template_name = 'superadmin/auditorcomment_addnew.html'
#     success_url = 'QMS:auditscheduleview'
#
#     def get_context_data(self, **kwargs):
#             context = super(Auditorcommentaddnew, self).get_context_data(**kwargs)
#             context["form"] = Auditor_commentsForm()
#             return context
#
#     def post(self, request, *args, **kwargs):
#         model = Audit_comments()
#         form = Auditor_commentsForm(request.POST)
#         if  form.is_valid():
#             a_type = request.POST.getlist('audittype')
#             cls_no = request.POST.getlist('cls_refno')
#             desc = request.POST.getlist('description')
#             aud_cmt = request.POST.getlist('auditor_comments')
#             aud_sts = request.POST.getlist('auditor_status')
#             dept = request.POST.getlist('department')
#             id = request.POST.getlist('auditschedule_id')
#             wm_id = request.POST.getlist('workmanual_id')
#             c = len(aud_cmt) #take any variable lenth inside if condition
#             for i in range(c):
#                 instance = Audit_comments.objects.create(audittype=a_type[i],cls_refno=cls_no[i],description=desc[i],
#                                     auditor_comments=aud_cmt[i],auditor_status=aud_sts[i],department=dept[i],
#                                     auditschedule_id = id[i],workmanual_id=wm_id[i])
#                 # instance.save()
#         return HttpResponseRedirect(self.get_success_url())
#
#     def get_success_url(self):
#        return reverse_lazy(self.success_url)
#

class AuditorcommentUpdate(UpdateView):
     model = Audit_comments
     form_class = Auditor_commentsForm
     success_url = 'QMS:auditscheduleview'
     template_name = 'superadmin/auditorcomment_update.html'
     def get_context_data(self, **kwargs):
             context = super(AuditorcommentUpdate, self).get_context_data(**kwargs)
             context["workmanual"] = WorkManual.objects.all()
             context["auditorcomments"] = Audit_comments.objects.get(pk=self.kwargs.get("pk"))
             return context

     def post(self, request, *args, **kwargs):
         form = Auditor_commentsForm(request.POST)
         if form.is_valid():
             Audit_comments.objects.filter(pk=self.kwargs.get("pk")).update(
             auditor_comments = request.POST.get('auditor_comments'),
             auditor_status = request.POST.get('auditor_status'),
             department = request.POST.get('department'),
             auditee_comments = request.POST.get('auditee_comments'),
             auditee_status = request.POST.get('auditee_status')
             )
         return HttpResponseRedirect(self.get_success_url())

     def get_success_url(self):
        return reverse_lazy(self.success_url)


class AuditorcommentDelete(DeleteView):
    model = Audit_comments
    success_url = 'QMS:auditscheduleview'
    template_name = 'superadmin/auditorcomment_confirm_delete.html'

    def get_object(self, queryset=None):
        """ Hook to ensure object is owned by request.user. """
        obj = super(AuditorcommentDelete, self).get_object()
        return obj

    def get_success_url(self):
        return reverse_lazy(self.success_url)


class AuditeecommentCreate(CreateView):
    model = Audit_comments
    form_class = Auditee_commentsForm
    template_name = 'superadmin/auditeecomment_form.html'
    success_url = 'QMS:auditscheduleview'

    def get_success_url(self):
       return reverse_lazy(self.success_url)

    def get_context_data(self, **kwargs):
        context = super(AuditeecommentCreate, self).get_context_data(**kwargs)
        context["auditschedule"] = Auditschedule.objects.get(pk=self.kwargs.get("pk"))
        context["auditcomments"] = Audit_comments.objects.all()
        context["form"] = Auditee_commentsForm()
        return context

    def post(self, request, *args, **kwargs):
        form = Auditee_commentsForm(request.POST)
        if form.is_valid():
            id = request.POST.getlist('id')
            aude_com = request.POST.getlist('auditee_comments')
            aude_sts = request.POST.getlist('auditee_status')
            c = len(id)
            for k in range(c):
                Audit_comments.objects.filter(pk=id[k]).update(auditee_comments = aude_com[k],auditee_status = aude_sts[k])
        return HttpResponseRedirect(self.get_success_url())


class AuditeecommentUpdate(UpdateView):
     model = Audit_comments
     form_class = Auditee_commentsForm
     success_url = 'QMS:auditscheduleview'
     template_name = 'superadmin/auditeecomment_update.html'

     def get_context_data(self, **kwargs):
             context = super(AuditeecommentUpdate, self).get_context_data(**kwargs)
             context["auditcomments"] = Audit_comments.objects.get(pk=self.kwargs.get("pk"))
             return context

     def post(self, request, *args, **kwargs):
         form = Auditee_commentsForm(request.POST)
         if form.is_valid():
             Audit_comments.objects.filter(pk=self.kwargs.get("pk")).update(
             auditee_comments = request.POST.get('auditee_comments'),
             auditee_status = request.POST.get('auditee_status'),
             )
         return HttpResponseRedirect(self.get_success_url())

     def get_success_url(self):
        return reverse_lazy(self.success_url)


class VerifycommentCreate(CreateView):
    model = Audit_comments
    form_class = Verified_commentsForm
    template_name = 'superadmin/verifycomment_form.html'
    success_url = 'QMS:auditscheduleview'

    def get_context_data(self, **kwargs):
        context = super(VerifycommentCreate, self).get_context_data(**kwargs)
        context["auditschedule"] = Auditschedule.objects.get(pk=self.kwargs.get("pk"))
        context["auditcomments"] = Audit_comments.objects.all()
        context["form"] = Verified_commentsForm()
        return context

    def post(self, request, *args, **kwargs):
        form = Verified_commentsForm(request.POST)
        if form.is_valid():
            id = request.POST.getlist('id')
            aude_com = request.POST.getlist('verified_comments')
            aude_sts = request.POST.getlist('verified_status')
            c = len(id)
            for k in range(c):
                Audit_comments.objects.filter(pk=id[k]).update(verified_comments = aude_com[k],verified_status = aude_sts[k])
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
       return reverse_lazy(self.success_url)


class VerifycommentUpdate(UpdateView):
     model = Audit_comments
     form_class = Verified_commentsForm
     success_url = 'QMS:auditscheduleview'
     template_name = 'superadmin/verifycomment_update.html'

     def get_context_data(self, **kwargs):
             context = super(VerifycommentUpdate, self).get_context_data(**kwargs)
             context["auditcomments"] = Audit_comments.objects.get(pk=self.kwargs.get("pk"))
             return context

     def post(self, request, *args, **kwargs):
         form = Verified_commentsForm(request.POST)
         if form.is_valid():
             Audit_comments.objects.filter(pk=self.kwargs.get("pk")).update(
             verified_comments = request.POST.get('verified_comments'),
             verified_status = request.POST.get('verified_status'),
             )
         return HttpResponseRedirect(self.get_success_url())

     def get_success_url(self):
        return reverse_lazy(self.success_url)





# @transaction.atomic
# def get_initial(self):
#
#     auditschedule = Auditschedule.objects.get(pk=self.kwargs.get("pk"))
#     wrkman = WorkManual.objects.all()
#     model = Audit_comments()
#     # import pdb
#     # pdb.set_trace()
#     for wm in wrkman:
#         lis = [ o.audittype for o in wm.audit_typ.all()]
#         if auditschedule.schedule_auditype.audittype in lis:
#                 Audit_comments.objects.update_or_create(audittype = auditschedule.schedule_auditype.audittype,
#                                                 cls_refno = wm.cls_ref_no,
#                                                 description=wm.activity_title)
#         else:
#             lis.clear()
#     return self.initial.copy()
