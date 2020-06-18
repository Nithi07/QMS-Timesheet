from django.urls import path
from QMS.views import common
from QMS.views import auditorlist
from QMS.views import auditschedule
from QMS.views import empdetails
from QMS.views import workmanual
from QMS.views import auditcomment



app_name = 'QMS'


urlpatterns = [
    # path('cmt/',auditcomment.cmt,name='cmt'),

    path('homepage/',common.HomePage.as_view(),name='homepage' ),

    path('audittypeview/',common.AudittypeListview.as_view(),name='audittypeview' ),

    path('audittypecreate/',common.AudittypeCreate.as_view(),name='audittypecreate' ),

    path('audittypeupdate/<int:pk>/',common.AudittypeUpdate.as_view(),name='audittypeupdate'),

    path('audittypedelete/<int:pk>/',common.AudittypeDelete.as_view(),name='audittypedelete' ),

    path('emppositionview/',common.EmployePositionListview.as_view(),name='emppositionview' ),

    path('emppositionform/',common.EmployePositionCreate.as_view(),name='emppositionform' ),

    path('emppositionupdate/<int:pk>/',common.EmployePositionUpdate.as_view(),name='emppositionupdate'),

    path('emppositiondelete/<int:pk>/',common.EmployePositionDelete.as_view(),name='emppositiondelete' ),

    path('employedeptview/',common.EmployeDepartmentListview.as_view(),name='employedeptview' ),

    path('employedeptform/',common.EmployeDepartmentCreate.as_view(),name='employedeptform' ),

    path('employedeptupdate/<int:pk>/',common.EmployeDepartmentUpdate.as_view(),name='employedeptupdate'),

    path('employedeptdelete/<int:pk>/',common.EmployeDepartmentDelete.as_view(),name='employedeptdelete' ),

    path('auditorlistform/',auditorlist.AuditorlistCreate.as_view(),name='auditorlistform'),

    path('auditorlistview/',auditorlist.AuditorlistListview.as_view(),name='auditorlistview'),

    path('auditorlistupdate/<int:pk>/',auditorlist.AuditorlistUpdate.as_view(),name='auditorlistupdate'),

    path('auditorlistdelete/<int:pk>/',auditorlist.AuditorlistDelete.as_view(),name='auditorlistdelete'),

    path('auditscheduleform/',auditschedule.AuditscheduleCreate.as_view(),name='auditscheduleform'),

    path('auditscheduleview/',auditschedule.AuditscheduleListview.as_view(),name='auditscheduleview'),

    path('auditscheduleconfirmview/<int:pk>/',auditschedule.AuditscheduleConfirmListview.as_view(),name='auditscheduleconfirmview'),

    path('auditscheduleconfirmconfirm/<int:pk>/',auditschedule.AuditscheduleConfirmUpdate.as_view(),name='auditscheduleconfirmconfirm'),

    path('auditscheduleupdate/<int:pk>/',auditschedule.AuditscheduleUpdate.as_view(),name='auditscheduleupdate'),

    path('auditscheduledelete/<int:pk>/',auditschedule.AuditscheduleDelete.as_view(),name='auditscheduledelete'),


    path('auditorcommentform/<int:pk>/',auditcomment.AuditorcommentCreate.as_view(),name='auditorcommentform'),
    path('auditorcommentview/',auditcomment.AuditorcommentListview.as_view(),name='auditorcommentview'),
    path('auditorcommentaddnew/',auditcomment.Auditorcommentaddnew.as_view(),name='auditorcommentaddnew'),
    path('auditorcommentdelete/<int:pk>/',auditcomment.AuditorcommentDelete.as_view(),name='auditorcommentdelete'),
    path('auditorcommentupdate/<int:pk>/',auditcomment.AuditorcommentUpdate.as_view(),name='auditorcommentupdate'),
    path('auditeecommentform/<int:pk>/',auditcomment.AuditeecommentCreate.as_view(),name='auditeecommentform'),
    path('auditeecommentupdate/<int:pk>/',auditcomment.AuditeecommentUpdate.as_view(),name='auditeecommentupdate'),
    path('verifycommentform/<int:pk>/',auditcomment.VerifycommentCreate.as_view(),name='verifycommentform'),

    path('empdetailsform/',empdetails.EmployeeDetailsCreate.as_view(),name='empdetailsform'),

    path('empdetailsview/',empdetails.EmployeeDetailsListview.as_view(),name='empdetailsview'),

    path('empdetailsupdate/<int:pk>/',empdetails.EmployeeDetailsUpdate.as_view(),name='empdetailsupdate'),

    path('empdetailsdelete/<int:pk>/',empdetails.EmployeeDetailsDelete.as_view(),name='empdetailsdelete'),

    path('workmanualform/',workmanual.WorkManualCreate.as_view(),name='workmanualform'),

    path('workmanualview/',workmanual.WorkManualListview.as_view(),name='workmanualview'),

    path('workmanualupdate/<int:pk>/',workmanual.WorkManualUpdate.as_view(),name='workmanualupdate'),

    path('workmanualdelete/<int:pk>/',workmanual.WorkManuaDelete.as_view(),name='workmanualdelete'),

    path('workmanualaddnew/<int:pk>/',workmanual.WorkManualaddnewCreate.as_view(),name='workmanualaddnew'),


   ]
