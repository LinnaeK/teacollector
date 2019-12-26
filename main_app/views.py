from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import DrinkingForm
from .models import Tea, Store, Drinking 

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def teas_index(request):
    teas = Tea.objects.filter(user=request.user)
    return render(request, 'teas/index.html', {'teas': teas})

@login_required
def teas_detail(request, tea_id):
    tea = Tea.objects.get(id=tea_id)
    stores_tea_doesnt_have = Store.objects.exclude(id__in = tea.stores.all().values_list('id'))
    drinking_form = DrinkingForm()
    return render(request, 'teas/detail.html', { 
        'tea': tea,
        'drinking_form': drinking_form,
        'stores': stores_tea_doesnt_have
         })

class TeaCreate(LoginRequiredMixin, CreateView):
    model = Tea
    fields = ['name', 'category', 'water_temp', 'steeping_time', 'notes']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TeaUpdate(LoginRequiredMixin, UpdateView):
    model = Tea
    fields = ['name', 'category', 'water_temp', 'steeping_time', 'notes']

    def form_valid(self, form):
        return super().form_valid(form)

class TeaDelete(LoginRequiredMixin, DeleteView):
    model = Tea
    success_url = '/teas/'

@login_required
def add_drinking(request, tea):
    form = DrinkingForm(request.POST)
    print(form)
    if form.is_valid():
        new_drinking = form.save(commit=False)
        new_drinking.tea_id = tea
        new_drinking.save()
    return redirect('detail', tea_id=tea)

@login_required
def assoc_store(request, tea_id, store_id):
    Tea.objects.get(id=tea_id).stores.add(store_id)
    return redirect('detail', tea_id=tea_id)

@login_required
def unassoc_store(request, tea_id, store_id):
    Tea.objects.get(id=tea_id).stores.remove(store_id)
    return redirect('detail', tea_id=tea_id)

class StoreList(LoginRequiredMixin, ListView):
    model = Store

class StoreCreate(LoginRequiredMixin, CreateView):
    model = Store
    fields = ['name', 'website', 'address', 'city', 'phone']

class StoreUpdate(LoginRequiredMixin, UpdateView):
    model = Store
    fields = ['name', 'website', 'address', 'city', 'phone']

class StoreDetailView(LoginRequiredMixin, DetailView):
    model = Store
    
class StoreDelete(LoginRequiredMixin, DeleteView):
    model = Store
    success_url = '/stores/'

@login_required
def signup(request):
    error_message=''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)