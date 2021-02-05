from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse
from .forms import ClientForm, AddCarForm, CarDamageForm, AddReservation, ReservationOptionsForm, UserAddForm, LoginUser
from .models import Car, CarDamage, Reservation, Client, ReservationOptions, ClientAsk
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.



########################################################################################################################

#                                        DODAWANIE SAMOCHODU


class AddCarView(PermissionRequiredMixin, View):
    permission_required = 'car_rental_app.add_car'
    def get(self, request):
        form = AddCarForm
        return render(request, "Add_car.html", {"form": form})

    def post(self, request):
        form = AddCarForm(request.POST)
        if form.is_valid():
            added_car = Car.objects.create(brand=form.cleaned_data['brand'],
                                           car_model=form.cleaned_data['car_model'],
                                           vin=form.cleaned_data['vin'],
                                           reg_plates=form.cleaned_data['reg_plates'],
                                           car_inspection=form.cleaned_data['car_inspection'],\
                                           insurence=form.cleaned_data['insurence'],
                                           millage=form.cleaned_data['millage'],
                                           next_service=form.cleaned_data['next_service'],\
                                           p_capicity=form.cleaned_data['p_capicity'],
                                           body_type=form.cleaned_data['body_type'],
                                           car_class=form.cleaned_data['car_class'],\
                                           num_of_doors=form.cleaned_data['num_of_doors'],
                                           eng_capicity=form.cleaned_data['eng_capicity'],\
                                           damage=form.cleaned_data['damage'],
                                           status=form.cleaned_data['status'],
                                           hp=form.cleaned_data['hp'],\
                                           d_production=form.cleaned_data['y_production'])

            return redirect(f'Car_view/{added_car.id}')
        else:
            return render(request, "Add_car.html", {"form": form})


########################################################################################################################

#                                        WIDOK SAMOCHODU


class CarView(PermissionRequiredMixin, View):
    permission_required = 'car_rental_app.view_car'
    def get(self, request, car_id):
        car = Car.objects.get(id=car_id)
        reservations = Reservation.objects.get(id=car_id)
        damages = CarDamage.objects.filter(car=car_id)
        return render(request, "Car_view.html", {"car":car, "damages":damages, "reservations":reservations})



########################################################################################################################

#                                        DODAWANIE SZKODY

class AddDamgeView(PermissionRequiredMixin, View):
        permission_required = 'car_rental_app.add_damage'
        def get(self, request):
            form = CarDamageForm
            return render(request, "Add_damage.html", {"form": form})

        def post(self, request):
            form = CarDamageForm(request.POST)
            if form.is_valid():
                added_damage = CarDamage.objects.create(car=form.cleaned_data["car"],
                                               driver=form.cleaned_data["driver"],
                                               date=form.cleaned_data['date'],
                                               d_status=form.cleaned_data['d_status'],
                                               title=form.cleaned_data['title'],
                                               d_type=form.cleaned_data['d_type'],
                                               d_note=form.cleaned_data['d_note']
                                               )
                return redirect(f'damage/{form.cleaned_data["added_damage"].id}')
            else:
                return render(request, "Add_damage.html", {"form": form})



########################################################################################################################

#                                        DODAWANIE REZERWACJI


class AddReservationView(PermissionRequiredMixin, View):
    permission_required = 'car_rental_app.add_reservation'
    def get(self, request):
        form = AddReservation
        return render(request, "Add_Reservation.html",{"form": form})

    def post(self, request):
        form = AddReservation(request.POST)
        if form.is_valid():
            added_reservation = Reservation.objects.create(car_id=form.cleaned_data["car.id"],
                                                           client_id=form.cleaned_data["client.id"],
                                                           start_date=form.cleaned_data["startdate"],
                                                           end_date=form.cleaned_data["end_date"],
                                                           start_millage=form.cleaned_data['start_millage'],
                                                           end_millage=form.cleaned_data['end_millage'],
                                                           millage_done=form.cleaned_data['millage_done'],
                                                           reservation_status=form.cleaned_data['reservation_status'])
            return redirect(f'Reservation_view/{added_reservation.id}')
        else:
            return render(request, "Add_Reservation.html", {"form": form})


########################################################################################################################

#                                        DODAWANIE KLIENTA


class ClientFormView(PermissionRequiredMixin, FormView):
    permission_required = 'car_rental_app.add_client'
    def get(self, request):
        form = ClientForm
        return render(request, "client_form.html", {"form":form})

    def post(self, request):
        form = ClientForm(request.POST)
        if form.is_valid():
            added_client = Client.objects.create(
                name=form.cleaned_data["name"],
                surname=form.cleaned_data["surname"],
                strname=form.cleaned_data["strname"],
                homenum=form.cleaned_data["homenum"],
                flatnum=form.cleaned_data["flatnum"],
                idnum=form.cleaned_data["idnum"],
                dlnum=form.cleaned_data["dlnum"],
                pesel=form.cleaned_data["pesel"],
                email=form.cleaned_data["email"],
                phonenum=form.cleaned_data["phonenum"],
            )
            return redirect(f'/Client/{added_client.id}')
        else:
            return render(request, "client_form.html", {"form": form})


########################################################################################################################

#                                        KLIENTVIEW

class ClientView(PermissionRequiredMixin,View):
    permission_required = 'car_rental_app.view_client'
    def get(self, request, client_id):
        client = Client.objects.get(id=client_id)
        reservations = Reservation.objects.filter(driver=client_id)
        # damages = CarDamage.objects.get(client=client_id)
        return render(request, "Client.html", {"client":client, "reservations":reservations})


########################################################################################################################

#                                        CARSVIEW

class CarsView(PermissionRequiredMixin,View):
    permission_required = 'car_rental_app.view_car'
    def get(self, request):
        cars = Car.objects.all()
        return render(request, "cars_view.html", {"cars":cars})


class CarUpdateViewByAutoView(PermissionRequiredMixin, UpdateView):
    permission_required = 'car_rental_app.change_car'
    model = Car
    template_name = 'edit_car.html'
    fields = ['brand', 'car_model', 'car_class', 'body_type', 'eng_capicity', 'hp', 'd_production', 'reg_plates', 'vin', 'millage',
              'next_service', 'car_inspection', 'insurence', 'p_capicity', 'num_of_doors', 'damage', 'status']
    success_url = '/cars_view/'


########################################################################################################################

#                                        CLIENTEDIT

class ClientUpdateViewByAutoView(PermissionRequiredMixin, View):
    permission_required = 'car_rental_app.change_client'
    model = Client
    template_name = 'edit_client.html'
    fields = ['name', 'surname', 'strname', 'homenum', 'flatnum', 'idnum', 'dlnum', 'pesel', 'email', 'phonenum']
    success_url = '/clients_view/'


########################################################################################################################

#                                        CLIENTSVIEW

class ClientsView(PermissionRequiredMixin, View):
    permission_required = 'car_rental_app.view_client'
    def get(self, request):
        clients = Client.objects.all()
        return render(request, "clients.html", {"clients":clients})


########################################################################################################################

#                                        CARDELETE

class CarDeleteViewByAutoView(PermissionRequiredMixin, View):
    permission_required = 'car_rental_app.delete_car'
    model = Car
    template_name = "car_confirm_delete.html"
    success_url = '/cars_view/'


########################################################################################################################

#                                        CLIENTDELETE

class ClientDeleteViewByAutoView(PermissionRequiredMixin, View):
    permission_required = 'car_rental_app.delete_client'
    model = Client
    template_name = 'client_confirm_delete.html'
    success_url = '/clients/'

########################################################################################################################

#                                        RESERVATIONEDIT

class ResrvationUpdateViewByAutoView(PermissionRequiredMixin, View):
    permission_required = 'car_rental_app.change_reservation'
    model = Client
    template_name = 'edit_reservation.html'
    fields = ['car', 'driver', 'start_date', 'end_date', 'start_millage', 'end_millage', 'reservation_status', 'reservation_options']
    success_url = '/Reservations/'


########################################################################################################################

#                                        RESERVATIONDELETE

class ReservationDeleteViewByAutoView(PermissionRequiredMixin, View):
    permission_required = 'car_rental_app.delete_reservation'
    model = Reservation
    template_name = "reservation_confirm_delete.html"
    success_url = '/reservations_view/'


########################################################################################################################

#                                        RESERVATIONSVIEW

class ResrvationsView(PermissionRequiredMixin, View):
    permission_required = 'car_rental_app.view_reservation'
    def get(self, request):
        reservations = Reservation.objects.all()
        return render(request, "Reservations.html", {"reservations":reservations })


########################################################################################################################

#                                        RESERVATION VIEW

class ReservationView(PermissionRequiredMixin, View):
    permission_required = 'car_rental_app.view_reservation'
    def get(self, request, reservation_id):
        reservation = Reservation.objects.get(id=reservation_id)
        resop = ReservationOptions.objects.get(id=reservation_id)
        return render(request, "Reservation.html", {"reservation":reservation, "resop":resop})

########################################################################################################################

#                                        DAMAGES EDIT

class DamagesUpdateViewByAutoView(PermissionRequiredMixin, View):
    permission_required = 'car_rental_app.change_cardamage'
    model = CarDamage
    template_name = 'edit_car_damage.html'
    fields = ['car', 'driver', 'date', 'd_status', 'title', 'd_type', 'd_note',]
    success_url = '/Damages/'

########################################################################################################################

#                                       DAMAGES VIEW

class DamagesView(PermissionRequiredMixin, View):
    permission_required = 'car_rental_app.view_cardamage'
    def get(self, request):
        damages = Reservation.objects.all()
        return render(request, "Damages.html", {"damages":damages})



########################################################################################################################

#                                        DAMAGE VIEW

class DamageView(View):
    def get(self, request, damage_id):
        damage = Reservation.objects.get(id=damage_id)
        return render(request, "damage.html", {"damage":damage })



########################################################################################################################
########################################################################################################################

#                                               RESERVATION OPTIONS

########################################################################################################################
########################################################################################################################

#                                               RESERVATION OPTIONS FORM

class OptionsAddFormView(PermissionRequiredMixin, View):
    permission_required = 'car_rental_app.add_reservationoptions'
    template_name = 'add_option.html'
    form_class = ReservationOptionsForm
    success_url = '/Reservations/'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


########################################################################################################################

#                                               RESERVATION OPTION VIEW

class OptionView(PermissionRequiredMixin,View):
    permission_required = 'car_rental_app.view_reservationoptions'
    def get(self, request, option_id):
        option = ReservationOptions.objects.get(id=option_id)
        return render(request, "option.html", {"option":option})


########################################################################################################################

#                                            OPTION DELETE

class OptionDeleteViewByAutoView(PermissionRequiredMixin, View):
    permission_required = 'car_rental_app.delete_reservationoptions'
    model = ReservationOptions
    template_name = "option_confirm_delete.html"
    success_url = '/reservations_view/'



########################################################################################################################

#                                            OPTION EDIT

class OptionUpdateViewByAutoView(PermissionRequiredMixin, View):
    permission_required = 'car_rental_app.change_reservationoptions'
    model = ReservationOptions
    template_name = 'option_edit.html'
    fields = ['reservation', 'child_seat', 'number_of_cs', 'additional_driver', 'abolition', 'insurence']
    success_url = '/Reservations/'





########################################################################################################################
########################################################################################################################

#                                            RESRVATION INQUIRY

class ResInqCreateViewByAutoView(CreateView):
    form = ClientAsk
    model = ClientAsk
    template_name = "res_inq_add.html"
    fields = ['car', 'start_date', 'end_date']
    def get_success_url(self):
        return reverse('up_res_inq', args=(self.object.id,))



class ResInqUpdateViewByAutoView(UpdateView):
    form = ClientAsk
    model = ClientAsk
    template_name = "edit_res_inq.html"
    fields = ['child_seat','number_of_cs', 'additional_driver', 'abolition', 'insurence']
    def get_success_url(self):
        return reverse('up_res_inq1', args=(self.object.id,))



class ResInq1UpdateViewByAutoView(UpdateView):
    form = ClientAsk
    model = ClientAsk
    template_name = "edit_res_inq1.html"
    fields = ['name','surname', 'email_q', 'phonenum_q']
    success_url = "/res_inq_added"


class ResInqDeleteViewByAutoView(DeleteView):
    model = ClientAsk
    template_name = "res_inq_confirm_delete.html"
    success_url = '/res_inq_view/'

class ResInqAllView(View):
    def get(self, request):
        res_inq_all = ClientAsk.objects.all()
        return render(request, "res_inq_all.html", {"res_inq_all":res_inq_all})

class ResInqView(View):
    def get(self, request, res_inq_id):
        res_inq = ClientAsk.objects.get(id=res_inq_id)
        return render(request, "res_inq_add.html/", {"res_inq":res_inq})

########################################################################################################################

#                                            ADD USER


class AddUserView(View):
    def get(self, request):
        form = UserAddForm()
        return render(request, "add_user.html", {'form': form})
    def post(self, request):
        form = UserAddForm(request.POST)
        if form.is_valid():
            User.objects.create_user(username=form.cleaned_data['login'],
                                     password=form.cleaned_data['password'],
                                     email=form.cleaned_data['email'],
                                     first_name=form.cleaned_data['first_name'],
                                     last_name=form.cleaned_data['last_name'])
            return redirect('/login/')
        else:
            return render(request, "add_user.html", {'form': form})


########################################################################################################################

#                                            USER LOG OUT

class LogOut(View):
    def get(self, request):
        logout(request)
        return redirect('/about_us')


########################################################################################################################

#                                            USER LOGIN

class LoginUserView(View):
    def get(self, request):
        form = LoginUser()
        return render(request, "login.html", {"form": form})
    def post(self, request):
        rec_form = LoginUser(request.POST)
        if rec_form.is_valid():
            user = authenticate(username = rec_form.cleaned_data["login"], password = rec_form.cleaned_data["password"])
            if user:
                login(request, user)
                return redirect('/about_us')
            else:
                return render(request, "login.html", {'form':rec_form})
        else:
            return render(request, "login.html", {'form': rec_form})


########################################################################################################################

#                                           STATIC VIEWS

class AboutUsView(View):
    def get(self, request):
        return render(request, "about_us.html")

class FleetView(View):
    def get(self, request):
        return render(request, "fleet_view.html")