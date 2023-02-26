from users.models import Userform
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from excursions.models import Excursion
import csv
from django.http import HttpResponse

# Create your views here.
@login_required
def participant(request):
    if request.method == 'GET':
        user = request.user
        excursion= Excursion.objects.filter(is_available=True)
        events = [event[0] for event in Userform.EVENTS]
        context = {
            'user': user,
            'excursion': excursion,
            'events': events,
        }
        return render(request, 'pages/participant.html', context=context)
    if request.method == 'POST':
        guest = Userform()

        guest.staff = request.user

        guest.first_name = request.POST['first_name']
        guest.last_name = request.POST['last_name']
        guest.phone = request.POST['phone']
        guest.excursion = Excursion.objects.get(id=request.POST['excursion'])
        guest.event = request.POST['event']
        guest.email = request.POST['email']
        guest.pg_agreement = request.POST['pg_agreement']
        
        # for ecx in excursions: # (variable) excursions: Unbound
        #     if ecx.id == int(guest.excursion.id):
        #         ecx.number_of_visitors += 1 # RelatedObjectDoesNotExist at /participant Userform has no excursion.
        guest.save()
        # excursions.save()
        return render(request, 'pages/index.html')
        

@login_required
def search_participant(request):
    guests = Userform.objects.all()
    query_string = ''

    # Search
    search = request.GET.get('search', '')
    if search:
        guests = guests.filter(
            first_name__icontains=search, 
            # last_name__icontains=search
            )
        query_string += f'&search={search}'

    # paginator
    paginator = Paginator(guests, len(guests))

    # filter
    filter = request.GET.get('filter', '')
    if filter:
        guests = guests.all()[:int(filter)]
        query_string += f'&filter={filter}'
        paginator = Paginator(guests, int(filter))



    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'guests': page_obj, #guests
        'query_string': query_string,
    }

    return render(request, 'pages/search.html', context=context)

@login_required
def download_csv(request):
    guests = Userform.objects.all()
    fields = ['id', 'Имя', 'Фамилия', 'Телефон', 'Email', 'Зарегистрирован', 'Экскурсия', 'Статус отправки email', 'Статус доставки email', 'Событие', 'Имя персонала']
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="guests.csv"'

    writer = csv.writer(response, csv.excel_tab)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow(fields)
    for guest in guests:
            data = [guest.pk, guest.first_name, guest.last_name, guest.phone, guest.email, guest.registered_at, guest.excursion, guest.email_status, guest.email_send, guest.event, f'{guest.staff.first_name} {guest.staff.last_name}']
            writer.writerow(data)
    
    return response