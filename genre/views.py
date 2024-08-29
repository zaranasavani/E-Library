from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Collection,Piece
from django.views import generic
from django.contrib.auth import login



# Create your views here.

# using generic class
class index(generic.ListView):
    template_name = "genre\indextemplate.html"

    def get_queryset(self):
        return Collection.objects.all()


class collections(generic.DetailView):
    model = Collection
    template_name = "genre/collectionstemplate.html"

class book_detail(generic.DetailView):
    model = Piece
    template_name = "genre/bookdetailtemplate.html"

def cart(request):
    if request.method == 'POST':
        piece_id = request.POST.get('piece_id')
        quantity = int(request.POST.get('quantity', 1))
        
        piece = get_object_or_404(Piece, id=piece_id)
        
        if 'cart' not in request.session:
            request.session['cart'] = {}
        
        cart = request.session['cart']
        if piece_id in cart:
            cart[piece_id] += quantity
        else:
            cart[piece_id] = quantity
        
        request.session.modified = True
        
        messages.success(request, f"{piece.title} added to cart.")
        
        return redirect('view_cart')
    
    return redirect('index')

def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0
    for piece_id, quantity in cart.items():
        piece = get_object_or_404(Piece, id=piece_id)
        subtotal = piece.price * quantity
        total += subtotal
        cart_items.append({
            'piece': piece,
            'quantity': quantity,
            'subtotal': subtotal
        })
    
    context = {
        'cart_items': cart_items,
        'total': total
    }
    return render(request, 'genre/carttemplate.html', context)

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

