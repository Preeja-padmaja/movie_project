from django.http import HttpResponse
from django.shortcuts import render, redirect

from movie_app.forms import movie_form
from movie_app.models import movie_table



# Create your views here.
def movie_first_fun(request):
    movies=movie_table.objects.all()
    #context={'movie_list':movies}
    return render(request,'index.html',{'values':movies})
def detail_view(request,movie_id):
    movies = movie_table.objects.get(id=movie_id)
    #return HttpResponse("This is movie number %s " % movie_id)
    return render(request,'detail.html',{'movies':movies})

def add_movie(request):
    if  request.method=='POST':
        m_name=request.POST.get('m_name',)
        desc=request.POST.get('desc',)
        year = request.POST.get('year',)
        image= request.FILES['image']
        if m_name==""or desc==""or year=="" :
            return render(request, 'add_movie.html', {'message': "Please Fill The Fields"})
        else:
            movie=movie_table(name=m_name,desc=desc,year=year,image=image)
            movie.save()
            return redirect('/')
    return render(request, 'add_movie.html',)
def update(request,id):
    movie=movie_table.objects.get(id=id)
    form=movie_form(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'update.html',{'form':form,'movie':movie})
def delete(request,id):
    if request.method=="POST":
        movie=movie_table.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,"delete.html")
