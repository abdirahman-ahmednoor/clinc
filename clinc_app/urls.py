from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views 
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  path('', views.index, name="index"),
  path('accounts/login/',views.login,name='login'),
  path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/logout.html'),name='logout'),
  path('search',views.search,name='search'),


  path('add_patient', views.add_patient,name='add_patient'),
  path('patients', views.patients,name='patients'),
  path('update_patient/<int:patient_id>', views.update_patient,name='update_patient'),
  path('delete_patient/<int:patient_id>', views.delete_patient,name='delete_patient'),
  path('patient_details/<int:patient_id>',views.patient_details,name='patient_details'),
  path('export_patients',views.export_patients,name='export_patients'),

  path('add_appointment', views.add_appointment,name='add_appointment'),
  path('appointments', views.appointments,name='appointments'),
  path('update_appointment/<int:appointment_id>', views.update_appointment,name='update_appointment'),
  path('delete_appointment/<int:appointment_id>', views.delete_appointment,name='delete_appointment'),
  path('appointment_details/<int:appointment_id>',views.appointment_details,name='appointment_details'),
  path('export_appointments',views.export_appointments,name='export_appointments'),

  path('add_prescription', views.add_prescription,name='add_prescription'),
  path('prescriptions', views.prescriptions,name='prescriptions'),
  path('update_prescription/<int:prescription_id>', views.update_prescription,name='update_prescription'),
  path('delete_prescription/<int:prescription_id>', views.delete_prescription,name='delete_prescription'),
  path('prescription_details/<int:prescription_id>',views.prescription_details,name='prescription_details'),
  path('export_prescriptions',views.export_prescriptions,name='export_prescriptions'),

  path('add_drug', views.add_drug,name='add_drug'),
  path('drugs', views.drugs,name='drugs'),
  path('update_drug/<int:drug_id>', views.update_drug,name='update_drug'),
  path('delete_drug/<int:drug_id>', views.delete_drug,name='delete_drug'),
  path('drug_details/<int:drug_id>',views.drug_details,name='drug_details'),
  path('export_drugs',views.export_drugs,name='export_drugs'),

  path('add_health_history', views.add_health_history,name='add_health_history'),
  path('history', views.history,name='history'),
  path('update_history/<int:history_id>', views.update_history,name='update_history'),
  path('delete_history/<int:history_id>', views.delete_history,name='delete_history'),
  path('history_details/<int:history_id>',views.history_details,name='history_details'),
  path('export_histories',views.export_histories,name='export_histories'),


  path('add_feedback', views.add_feedback,name='add_feedback'),
  path('feedback', views.feedback,name='feedback'),
  path('update_feedback/<int:feedback_id>', views.update_feedback,name='update_feedback'),
  path('delete_feedback/<int:feedback_id>', views.delete_feedback,name='delete_feedback'),
  path('feedback_details/<int:feedback_id>',views.feedback_details,name='feedback_details'),
  path('export_feedbacks',views.export_feedbacks,name='export_feedbacks'),

  path('add_visit', views.add_visit,name='add_visit'),
  path('visits', views.visits,name='visits'),
  path('update_visit/<int:visit_id>', views.update_visit,name='update_visit'),
  path('delete_visit/<int:visit_id>', views.delete_visit,name='delete_visit'),
  path('visit_details/<int:visit_id>',views.visit_details,name='visit_details'),
  path('export_visits',views.export_visits,name='export_visits'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
