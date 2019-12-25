from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .forms import DrinkingForm
from .models import Tea, Store, Drinking 

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def teas_index(request):
    teas = Tea.objects.all()
    return render(request, 'teas/index.html', {'teas': teas})

def teas_detail(request, tea_id):
    tea = Tea.objects.get(id=tea_id)
    stores_tea_doesnt_have = Store.objects.exclude(id__in = tea.stores.all().values_list('id'))
    drinking_form = DrinkingForm()
    return render(request, 'teas/detail.html', { 
        'tea': tea,
        'drinking_form': drinking_form,
        'stores': stores_tea_doesnt_have
         })

class TeaCreate(CreateView):
    model = Tea
    fields = ['name', 'category', 'water_temp', 'steeping_time', 'notes']

    def form_valid(self, form):
        return super().form_valid(form)

class TeaUpdate(UpdateView):
    model = Tea
    fields = ['name', 'category', 'water_temp', 'steeping_time', 'notes']

    def form_valid(self, form):
        return super().form_valid(form)

class TeaDelete(DeleteView):
    model = Tea
    success_url = '/teas/'

def add_drinking(request, tea):
    form = DrinkingForm(request.POST)
    print(form)
    if form.is_valid():
        new_drinking = form.save(commit=False)
        new_drinking.tea_id = tea
        new_drinking.save()
    return redirect('detail', tea_id=tea)

def assoc_store(request, tea_id, store_id):
    Tea.objects.get(id=tea_id).stores.add(store_id)
    return redirect('detail', tea_id=tea_id)

class StoreList(ListView):
    model = Store

class StoreCreate(CreateView):
    model = Store
    fields = ['name', 'website', 'address', 'city', 'phone']

class StoreUpdate(UpdateView):
    model = Store
    fields = ['name', 'website', 'address', 'city', 'phone']

class StoreDetailView(DetailView):
    model = Store
    
class StoreDelete(DeleteView):
    model = Store
    success_url = '/stores/'



