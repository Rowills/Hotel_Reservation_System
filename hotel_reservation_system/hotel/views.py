from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import Room
from django.contrib.auth.decorators import login_required

# List Rooms
@login_required
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'hotel/room_list.html', {'rooms': rooms})

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Room
from django.contrib.auth.decorators import login_required

@login_required
def room_add(request):
    if request.method == 'POST':
        room_id = request.POST.get('room_id', '').strip()
        room_type = request.POST.get('room_type', '')
        capacity = request.POST.get('capacity', '')
        price_per_night = request.POST.get('price_per_night', '')

        # Check if room_id already exists
        if Room.objects.filter(room_id=room_id).exists():
            messages.error(request, "Room ID already exists. Please choose a different Room ID.")
            return redirect('room_add')  # Redirect to reload the form with the error message

        # Create room if validation passes
        Room.objects.create(
            room_id=room_id,
            room_type=room_type,
            capacity=capacity,
            price_per_night=price_per_night
        )
        messages.success(request, "Room added successfully!")
        return redirect('room_list')  # Redirect to the list of rooms
    
    return render(request, 'hotel/room_form.html', {'ROOM_TYPES': Room.ROOM_TYPES})


@login_required
def room_edit(request, pk):
    room = get_object_or_404(Room, room_id=pk)
    if request.method == 'POST':
        room.room_type = request.POST['room_type']
        room.capacity = request.POST['capacity']
        room.price_per_night = request.POST['price_per_night']
        room.save()
        return redirect('room_list')
    return render(request, 'hotel/room_form.html', {'room': room, 'ROOM_TYPES': Room.ROOM_TYPES})

# Delete Room
@login_required
def room_delete(request, pk):
    room = get_object_or_404(Room, room_id=pk)
    room.delete()
    return redirect('room_list')

from .models import Guest

# List Guests
@login_required
def guest_list(request):
    guests = Guest.objects.all()
    return render(request, 'hotel/guest_list.html', {'guests': guests})

# Add Guest
@login_required
def guest_add(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        address = request.POST.get('address', '')  # Optional
        Guest.objects.create(name=name, email=email, phone_number=phone_number, address=address)
        return redirect('guest_list')
    return render(request, 'hotel/guest_form.html')

# Edit Guest
@login_required
def guest_edit(request, pk):
    guest = get_object_or_404(Guest, guest_id=pk)
    if request.method == 'POST':
        guest.name = request.POST['name']
        guest.email = request.POST['email']
        guest.phone_number = request.POST['phone_number']
        guest.address = request.POST.get('address', '')
        guest.save()
        return redirect('guest_list')
    return render(request, 'hotel/guest_form.html', {'guest': guest})

# Delete Guest
@login_required
def guest_delete(request, pk):
    guest = get_object_or_404(Guest, guest_id=pk)
    guest.delete()
    return redirect('guest_list')

from .models import Reservation

# List Reservations
@login_required
def reservation_list(request):
    reservations = Reservation.objects.select_related('room', 'guest')
    return render(request, 'hotel/reservation_list.html', {'reservations': reservations})

# Add Reservation
@login_required
def reservation_add(request):
    if request.method == 'POST':
        room_id = request.POST['room_id']
        guest_id = request.POST['guest_id']
        check_in_date = request.POST['check_in_date']
        check_out_date = request.POST['check_out_date']
        total_price = request.POST['total_price']
        payment_status = request.POST['payment_status']
        room = get_object_or_404(Room, room_id=room_id)
        guest = get_object_or_404(Guest, guest_id=guest_id)
        Reservation.objects.create(
            room=room, guest=guest,
            check_in_date=check_in_date,
            check_out_date=check_out_date,
            total_price=total_price,
            payment_status=payment_status
        )
        return redirect('reservation_list')
    return render(request, 'hotel/reservation_form.html')

# Edit Reservation
@login_required
def reservation_edit(request, pk):
    reservation = get_object_or_404(Reservation, reservation_id=pk)
    if request.method == 'POST':
        reservation.check_in_date = request.POST['check_in_date']
        reservation.check_out_date = request.POST['check_out_date']
        reservation.total_price = request.POST['total_price']
        reservation.payment_status = request.POST['payment_status']
        reservation.save()
        return redirect('reservation_list')
    return render(request, 'hotel/reservation_form.html', {'reservation': reservation})

# Delete Reservation
@login_required
def reservation_delete(request, pk):
    reservation = get_object_or_404(Reservation, reservation_id=pk)
    reservation.delete()
    return redirect('reservation_list')

from datetime import date
from django.db import models

@login_required
def occupancy_report(request):
    today = date.today()
    occupied_rooms = Reservation.objects.filter(
        check_in_date__lte=today,
        check_out_date__gte=today
    ).select_related('room', 'guest')
    return render(request, 'hotel/occupancy_report.html', {'occupied_rooms': occupied_rooms})

@login_required
def revenue_report(request):
    # Get filter parameters from the request
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    reservations = Reservation.objects.filter(payment_status='Paid')

    # Filter by date range if provided
    if start_date and end_date:
        reservations = reservations.filter(
            check_in_date__gte=start_date,
            check_out_date__lte=end_date
        )

    # Calculate total revenue
    total_revenue = reservations.aggregate(total=models.Sum('total_price'))['total'] or 0
    return render(request, 'hotel/revenue_report.html', {
        'reservations': reservations,
        'total_revenue': total_revenue,
        'start_date': start_date,
        'end_date': end_date
    })




# from django.contrib.auth import logout
# from django.shortcuts import redirect

# def custom_logout(request):
#     logout(request)  # Logout the user
#     return redirect('login')  # Redirect to the login page
