from django.urls import path
from . import views

# from django.urls import path
# from .views import custom_logout

# urlpatterns = [
#     path('accounts/logout/', custom_logout, name='logout'),
# ]

urlpatterns = [

    # Existing Room URLs
    path('rooms/', views.room_list, name='room_list'),
    path('rooms/add/', views.room_add, name='room_add'),
    path('rooms/edit/<str:pk>/', views.room_edit, name='room_edit'),
    path('rooms/delete/<str:pk>/', views.room_delete, name='room_delete'),
    
    # Guest URLs
    path('guests/', views.guest_list, name='guest_list'),
    path('guests/add/', views.guest_add, name='guest_add'),
    path('guests/edit/<int:pk>/', views.guest_edit, name='guest_edit'),
    path('guests/delete/<int:pk>/', views.guest_delete, name='guest_delete'),
]

urlpatterns += [
    # Reservation URLs
    path('reservations/', views.reservation_list, name='reservation_list'),
    path('reservations/add/', views.reservation_add, name='reservation_add'),
    path('reservations/edit/<int:pk>/', views.reservation_edit, name='reservation_edit'),
    path('reservations/delete/<int:pk>/', views.reservation_delete, name='reservation_delete'),
]

urlpatterns += [
    # Report URLs
    path('reports/occupancy/', views.occupancy_report, name='occupancy_report'),
    path('reports/revenue/', views.revenue_report, name='revenue_report'),
]
