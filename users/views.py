
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from .models import Userinfo, bills, transactions
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Sum
from django.db.models.functions import Abs
from django.urls import reverse_lazy



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


    def get_context_data(self, *args, **kwargs):
      context = super(BillsListView, self).get_context_data(*args, **kwargs)
      context['bTotal'] = bills.objects.filter(user_id=self.request.user).aggregate(Sum('bamount'))['bamount__sum'] or 0.00
      return context    



class BillsCreateView(LoginRequiredMixin, CreateView):
    model = bills
    success_url = '/users/billslist'
    fields = ['bname', 'bamount', 'brecipient', 'duedate']

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)


class BillsDetailView(DetailView):
    model = bills


class BillsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = bills
    success_url = '/users/billslist'
    fields = ['bname', 'bamount', 'brecpient', 'duedate']

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
    


class TranCreateView(LoginRequiredMixin, CreateView):
    model = transactions
    success_url = '/users/tactionslist'
    fields = ['tname', 'recipient', 'amount', 'date']
    
    #transactions.amount = transactions.amount * - 1
    #transactions.objects.update(amount=Abs(F('amount')))

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(TranCreateView, self).get_context_data(**kwargs) 
        context['bills_list'] = bills.objects.filter(user_id=self.request.user).all()
        return context



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



class billPay(LoginRequiredMixin, CreateView):

    template_name= 'billpay.html'
    model = transactions
    #def get_success_url(self):
     #   return reverse('bill-special')

    fields = ['tname', 'recipient', 'amount', 'date', 'special']
    
    #transactions.amount = transactions.amount * - 1
    #transactions.objects.update(amount=Abs(F('amount')))

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(billPay, self).get_context_data(**kwargs) 
        context['bills_list'] = bills.objects.filter(user_id=self.request.user).all()#order_by('-duedate')
        context['bTotal'] = bills.objects.filter(user_id=self.request.user).aggregate(Sum('bamount'))['bamount__sum'] or 0.00
        
        return context



class sDetailView(DetailView):
    model = transactions
    template_name= 'special.html'



def billspay(request):
    return render(request, 'billpay.html')


class MultipleModelView(TemplateView):
    template_name = 'landing.html'
    
   # def get_queryset(self): #gets only if user matches
    #    return self.model.objects.filter(user_id=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(MultipleModelView, self).get_context_data(**kwargs) 
        context['cBalance'] = transactions.objects.filter(user_id=self.request.user).aggregate(Sum('amount'))['amount__sum'] or 0.00
        context['bills_list'] = bills.objects.filter(user_id=self.request.user).all()
        return context

  
