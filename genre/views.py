from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Collection,Piece
from django.views import generic
from django.contrib.auth import login
from .forms import RegistrationForm


# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            return redirect('login')  # Redirect to a success page
    else:
        form = RegistrationForm()
    return render(request, 'genre/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')  # redirect to home page or another page
        else:
            messages.error(request, 'Invalid username or password')

    return render(request, 'genre/login.html')
# using generic class
class index(generic.ListView):
    template_name = "genre/indextemplate.html"

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

