from django.shortcuts import render, redirect
from .forms import BuyForm, TicketForm

# Create your views here.


def home(request):
    context = {}
    return render(request, 'base/index.html', context)

def about(request):
    context = {}
    return render(request, 'base/about.html', context)

def menu(request):
    context = {}
    return render(request, 'base/menu.html', context)

def buy(request):
    if request.method == 'POST':
        form = BuyForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()
            # Redirect or return a response
            return redirect('tickets')
    else:
        form = BuyForm()

    context = {'form': form}
    return render(request, 'base/buy.html', context)

def tickets(request):
    # if request.method == 'POST':
    #     form = TicketForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         # Adicione aqui a lógica de pagamento, se necessário.
    #         return redirect('sucesso')  # Redirecione para uma página de sucesso após a compra.
    # else:
    #     form = TicketForm()
    # context = {'form': form}
    context = {}
    return render(request, 'base/tickets.html', context)

