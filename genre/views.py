from django.shortcuts import render
from django.http import HttpResponse
from .models import Collection,Piece
from django.views import generic

# Create your views here.

# using generic class
class index(generic.ListView):
    template_name = "genre\genretemplate.html"

    def get_queryset(self):
        return Collection.objects.all()


class details(generic.DetailView):
    model = Collection
    template_name = "genre\detailtemplate.html"

class piece_detail(generic.DetailView):
    model = Piece
    template_name = "genre\piecedetailtemplate.html"




# using functions
# def index(request):
#     # return HttpResponse("<h1>Hello World </h1>")
#     all_collection = Collection.objects.all()
#     context ={
#         "all_collection" : all_collection
#     }
#     return render(request, "genre\genretemplate.html",context)
#
# def details(request, genre_id):
#     # return HttpResponse("<h1>the genre id is: " + str(genre_id) + "</h1>")
#     Citem = Collection.objects.get(pk=genre_id)
#     Pitem = Piece.objects.filter(collection=Citem)
#     context = {
#         "Pitem" : Pitem
#     }
#     return render(request, "genre\detailtemplate.html",context)
#
def aboutus(request):
    return HttpResponse("<h1> About Us Page </h1>")

