from django.shortcuts import render, redirect
from users.models import Userform
from excursions.models import Excursion
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
        filter = int(filter)
        guests = guests.filter(excursion__id=filter)
        query_string += f'&filter={filter}'

    # paginator
    paginator = Paginator(guests, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'guests': page_obj, #guests
        'query_string': query_string
    }
    return render(request, 'pages/emails.html', context=context)

@login_required
def send_email_to_guest(request, pk): # отправить конкретному гостю
    guest = Userform.objects.get(pk=pk)
    if guest.email_send == False:
        send_mail(
            '✨Excursion✨',
            f'Hey, {guest.first_name} {guest.last_name}! Here is the message. Your excursion is "{guest.excursion}" ',
            EMAIL_HOST_USER,
            [guest.email],
            fail_silently=False,
        )
        guest.email_send = True
        guest.email_status = True
    return redirect('emails')

@login_required
def send_email_to_exc_guests(request, excursion__id): # отправить всем, у кого соотв. экскурсия
    guests = Userform.objects.filter(excursion__id=excursion__id)
    for guest in guests:
        if guest.email_send == False:
            send_mail(
                '✨Excursion✨',
                f'Hey, {guest.first_name} {guest.last_name}! Here is the message. Your excursion is "{guest.excursion}" ',
                EMAIL_HOST_USER,
                [guest.email],
                fail_silently=False,
            )
            guest.email_send = True
            guest.email_status = True
    return redirect('emails')