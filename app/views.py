from django.shortcuts import render ,redirect
from .models import Project ,About,contact
from app.forms import Contact
# Create your views here.
def home(request):
    if request.method=='POST':
        form=Contact(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
            
    else:
          
        project=Project.objects.all()
        about=About.objects.all().first()
        form=Contact()

        return render(request,'index.html',{'project':project,'about':about,'form':form})
