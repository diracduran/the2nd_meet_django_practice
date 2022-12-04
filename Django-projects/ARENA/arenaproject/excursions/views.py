from django.shortcuts import render
from excursions.models import Excursion
from users.models import Userform
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def excursions(request):
    excursions = Excursion.objects.all()
    guests = Userform.objects.all()
    context = {
        'excursions': excursions,
        'guests': guests
    }
    for exc in excursions:
        date_time = f"{exc.weekdays} {exc.timelines}"
        for guest in guests:
            if guest.excursion == date_time:
                exc.number_of_visitors = guests.count(guest.excursion)

        if exc.number_of_visitors >= exc.total_visitors:
            exc.is_available = False
            exc.is_shown = False

    return render(request, 'pages/excursions.html', context=context)