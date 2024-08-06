from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index.as_view(),name="index"),                                 #this page open by default

    #genre/aboutus
    path('aboutus/',views.aboutus,name="aboutus"),

    #genre/1 (id of collection choosen by the user e.g. user choose fiction)
    path("<pk>",views.details.as_view(),name="details"),

    path('piece/<int:pk>/', views.piece_detail.as_view(), name='piece_detail'),

    path('',views.cart.as_view(),name="cart"),

    # path('userreg/',views.userreg.as_view(),name="userreg"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)