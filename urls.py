from django.urls import path
from . import views
from .views import PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, PostListView, \
    BillsCreateView, BillsDeleteView, BillsDetailView, BillsUpdateView, TranCreateView, \
    TranDeleteView, TranDetailView, TranUpdateView, BillsListView, TranListView, MultipleModelView




urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_, name='login'),
    path('signup/', views.signup_, name='signup'),
    #path('landing/', views.landingpage, name='landing'),
    path('landing/', MultipleModelView.as_view(), name='landing'),


    path('userlist/', PostListView.as_view(), name='user-list'),
    path('<int:pk>/', PostDetailView.as_view(), name='user-detail'),
    path('usernew/', PostCreateView.as_view(), name='user-create'),
    path('<int:pk>/update/', PostUpdateView.as_view(), name='user-update'),
    path('<int:pk>/delete/', PostDeleteView.as_view(), name='user-delete'),

    path('billslist/', BillsListView.as_view(), name='bill-list'),
    path('bills/<int:pk>/', BillsDetailView.as_view(), name='bills-detail'),
    path('billsnew/', BillsCreateView.as_view(), name='bills-create'),
    path('bills/<int:pk>/update/', BillsUpdateView.as_view(), name='bills-update'),
    path('bills/<int:pk>/delete/', BillsDeleteView.as_view(), name='bills-delete'),
    path('billspay/', views.billspay, name='billspay'),

    path('contact/', views.contact, name='contact'),

    path('tactionslist/', TranListView.as_view(), name='taction-list'),
    path('tactions/<int:pk>/', TranDetailView.as_view(), name='taction-detail'),
    path('tactionsnew/', TranCreateView.as_view(), name='taction-create'),
    path('tactions/<int:pk>/update/', TranUpdateView.as_view(), name='taction-update'),
    path('tactions/<int:pk>/delete/', TranDeleteView.as_view(), name='taction-delete'),

    path('logout/', views.logout_, name='logout'),
]