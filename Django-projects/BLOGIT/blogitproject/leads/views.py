from django.shortcuts import render
from leads.forms import LeadForm
from leads.models import Lead
from django.contrib import messages

# Create your views here.
def contact_page(request):
    if request.method == 'POST':
        form = LeadForm(data=request.POST)
        if form.is_valid():
            new_lead = Lead.objects.create(**form.cleaned_data)
            messages.success(request, '{}, your message has been successfully sent'.format(new_lead.name))
        else:
            messages.error(request, 'Somethong is going wrrong')

    form = LeadForm()
    context = {
        'form': form
    }
    return render(request, 'pages/contact.html', context=context)