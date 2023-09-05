from django.shortcuts import render,HttpResponse
from .models import Projects,Skills,Messages
from .forms import MessageForm

def Home(request):
    return render(request,template_name='home.html',context={
         "projects":Projects.objects.all(),
         "skillset":Skills.objects.all(),
         "form":MessageForm()
         }
         )         
                                           
def LeaveMessage(request):
        if request.method == 'POST':
              data=MessageForm(request.POST)
              if data.is_valid():
                   Messages( 
                    name=data.cleaned_data["name"],
                    email=data.cleaned_data["email"],
                    message=data.cleaned_data["message"]           
                    ).save()                                              
                   return HttpResponse("The request was successfull")