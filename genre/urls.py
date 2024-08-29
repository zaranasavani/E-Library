from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index.as_view(),name="index"), 
    # path('register/', views.register, name='register'),                                #this page open by default

    #genre/aboutus
    path('aboutus/',views.aboutus,name="aboutus"),

    #genre/1 (id of collection choosen by the user e.g. user choose fiction)
    path("<pk>",views.collections.as_view(),name="collections"),

    path('book/<int:pk>/', views.book_detail.as_view(), name='book_detail'),

    path('cart/',views.cart,name="cart"),
    path('view-cart/', views.view_cart, name='view_cart'),

    # path('userreg/',views.userreg.as_view(),name="userreg"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)