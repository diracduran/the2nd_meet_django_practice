from django.shortcuts import render
from users.models import Userform
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from arenaproject.settings import EMAIL_HOST_USER

@login_required
def emails(request):
    guests = Userform.objects.all()

    query_string = ''

    filter = request.GET.get('filter', '')
    if filter:
        guests = guests.filter(excursion=filter)
        query_string += f'&filter={filter}'

    # paginator
    paginator = Paginator(guests, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'guests': page_obj, #guests
        'query_string': query_string,
    }
    return render(request, 'pages/emails.html', context=context)

def send_email_to_guest(request, pk): # отправить конкретному гостю
    guest = Userform.objects.get(pk=pk)
    send_mail(
        'Subject here',
        'Here is the message.',
        EMAIL_HOST_USER,
        [guest.email],
        fail_silently=False,
    )
    guest.email_send = True
    guest.email_status = True
    return render(request, 'pages/emails.html')

def send_email_to_exc_guests(request, excursion): # отправить всем, у кого соотв. экскурсия
    guests = Userform.objects.filter(excursion=excursion)
    for guest in guests:
        send_mail(
            'Subject here',
            'Here is the message.',
            EMAIL_HOST_USER,
            [guest.email],
            fail_silently=False,
        )
        guest.email_send = True
        guest.email_status = True
    return render(request, 'pages/emails.html')

# def send_email_to_guest(request, guest):
#     guest = Userform.objects.filter(guest=guest)
#     send_mail(
#         'Subject here',
#         'Here is the message.',
#         'from@example.com',
#         [guest.email],
#         fail_silently=False,
#     )