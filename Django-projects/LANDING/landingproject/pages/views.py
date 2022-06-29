from django.shortcuts import render, redirect
from testimonial.models import Testimonial
from team.models import Team
from lead.models import Lead

# Create your views here.
def index(request):
    testimonials = Testimonial.objects.all()
    team = Team.objects.all()
    context = {
        'testimonials': testimonials,
        'team': team
    }
    return render(request, 'pages/index.html', context=context)

def send_message(request): 
    if request.method == 'POST': 
        new_message = Lead() 
        if 'name' in request.POST: 
            new_message.name = request.POST['name'] 
        if 'email' in request.POST: 
            new_message.email = request.POST['email'] 
        if 'subject' in request.POST: 
            new_message.subject = request.POST['subject'] 
        if 'message' in request.POST: 
            new_message.message = request.POST['message'] 
        new_message.save() 
        return redirect('index')