from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Userinfo, bills, transactions
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Sum
from django.template import loader

class PostListView (ListView):

    model = Userinfo

    def get_queryset(self): #gets only if user matches
        return self.model.objects.filter(author=self.request.user)


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Userinfo
    fields = ['fname', 'lname', 'address', 'city', 'state', 'zipcode',
              'dob', 'phone', 'email']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(DetailView):
    model = Userinfo



class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Userinfo
    success_url = '/users/userlist'
    fields = ['fname', 'lname', 'address', 'city', 'state', 'zipcode',
              'dob', 'phone', 'email']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Userinfo
    success_url = '/users/userlist'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



class BillsListView (ListView):

    model = bills

    def get_queryset(self): #gets only if user matches
        return self.model.objects.filter(user_id=self.request.user)



class BillsCreateView(LoginRequiredMixin, CreateView):
    model = bills
    success_url = '/users/billslist'
    fields = ['bname', 'bamount', 'duedate']

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)


class BillsDetailView(DetailView):
    model = bills


class BillsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = bills
    success_url = '/users/billslist'
    fields = ['bname', 'bamount', 'duedate']

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user_id:
            return True
        return False


class BillsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = bills
    success_url = '/users/billslist'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user_id:
            return True
        return False






class TranListView (ListView):

    model = transactions

    def get_queryset(self): #gets only if user matches
       return self.model.objects.filter(user_id=self.request.user)



    def get_context_data(self, *args, **kwargs):
        context = super(TranListView, self).get_context_data(*args, **kwargs)
        context['cBalance'] = transactions.objects.filter(user_id=self.request.user).aggregate(Sum('amount'))['amount__sum'] or 0.00
        return context    
    
    #context_object_name = 'transactions'
    
    #def get_context_data(self):
     #   cBalance = transactions.objects.all().aggregate(cBalance=Sum('amount'))
      #  return cBalance
    #cBalance = transactions.objects.all().aggregate(Sum('amount'))['amount__sum'] or 0.00



class TranCreateView(LoginRequiredMixin, CreateView):
    model = transactions
    success_url = '/users/tactionslist'
    fields = ['tname', 'recipient', 'amount', 'date']

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)


class TranDetailView(DetailView):
    model = transactions


class TranUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = transactions
    success_url = '/users/tactionslist'
    fields = ['tname', 'recipient', 'amount', 'date']

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user_id:
            return True
        return False


class TranDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = transactions
    success_url = '/users/tactionslist'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user_id:
            return True
        return False


def register(request):

    if request.method == 'POST':
        post = Userinfo()
        post.fname = request.POST.get('fname')
        post.lname = request.POST.get('lname')
        post.address = request.POST.get('address')
        post.city = request.POST.get('city')
        post.state = request.POST.get('state')
        post.zipcode = request.POST.get('zip_code')
        post.dob = request.POST.get('date of birth')
        post.phone = request.POST.get('phone number')
        post.email = request.POST.get('email')
        post.save()
        return redirect('/users/landing')

    else:
        return render(request, 'register.html')


def signup_(request):

    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()

            return redirect('home')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})


def login_(request):

    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
        else:
            return render(request, 'login.html', context={'form': form})
        return redirect('/users/landing')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', context={'form': form})


def logout_(request):
    logout(request)
    return redirect('home')


def landingpage(request):
    if request.user.is_authenticated:
        return render(request, 'landing.html')
    else:
        return redirect('login')


def index(request):
    return HttpResponse("Users Homepage")


def billspay(request):
    return render(request, 'billpay.html')
