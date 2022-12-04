from django.urls import path
from emails import views

urlpatterns = [
    path('emails/', views.emails, name='emails'),
    path('emails/email/<slug:pk>', views.send_email_to_guest, name='send_email_to_guest'),
    path('emails/email/excursion/<slug:excursion>', views.send_email_to_exc_guests, name='send_email_to_exc_guests')
]
