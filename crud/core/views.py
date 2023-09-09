from django.shortcuts import render,redirect
from django.views import View
from.models import student
from .forms import AddstudentFrom

# Create your views here.

class Home(View):
      def get(self,request):
            stu_data=student.objects.all()
            return render(request,"home.html",{'studata':stu_data})

class Add_student(View):
      

      def get(self,request):
            fm = AddstudentFrom()
            return render(request,"Add.html",{'form':fm})

      def post(self,request):
            fm= AddstudentFrom(request.POST)
            if fm.is_valid():
                  fm.save()
                  return redirect('/')
            else:
                   return render(request,"Add.html",{'form':fm})

class Delete(View):
      def post(self,request):
            data = request.POST
            id = data.get("id")
            studata = student.objects.get(id=id)
            studata.delete()
            return redirect('/')