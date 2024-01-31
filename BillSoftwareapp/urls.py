from . import views
from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('service', views.service, name='service'),
    path('register', views.register, name='register'),
    path('registercompany', views.registercompany, name='registercompany'),
    path('registerstaff', views.registerstaff, name='registerstaff'),
    path('login', views.login, name='login'),
    path('registeruser', views.registeruser, name='registeruser'),
    path('add_company', views.add_company, name='add_company'),
    path('add_item', views.add_item, name='add_item'),
    path('staff_registraction', views.staff_registraction, name='staff_registraction'),
    path('homepage', views.homepage, name='homepage'),
    path('staffhome', views.staffhome, name='staffhome'),
    path('loginurl', views.loginurl, name='loginurl'),
    path('logout', views.logout, name='logout'),
    path('save_item', views.save_item,name='save_item'),
    path('base', views.base, name='base'),
    path('profile', views.profile, name='profile'),
    path('staffprofile',views.staffprofile,name='staffprofile'),
    path('view_purchasebill', views.view_purchasebill, name='view_purchasebill'),
    path('add_purchasebill', views.add_purchasebill, name='add_purchasebill'),
    path('create_purchasebill', views.create_purchasebill, name='create_purchasebill'),
    path('show_purchasebill/<int:id>/', views.show_purchasebill, name='show_purchasebill'),
    path('savecustomer', views.savecustomer, name='savecustomer'),
    path('cust_dropdown', views.cust_dropdown, name='cust_dropdown'),
    path('saveitem', views.saveitem, name='saveitem'),
    path('item_dropdown', views.item_dropdown, name='item_dropdown'),
    path('itemdetails', views.itemdetails, name='itemdetails'),
    path('custdata',views.custdata,name='custdata'),
    path('show_purchasebill/<int:id>/', views.show_purchasebill, name='show_purchasebill'),
    path('edit_purchasebill/<int:id>',views.edit_purchasebill,name='edit_purchasebill'),
    path('update_purchasebill/<int:id>',views.update_purchasebill,name='update_purchasebill'),
    path('details_purchasebill/<int:id>',views.details_purchasebill,name='details_purchasebill'),
    path('history_purchasebill/<int:id>',views.history_purchasebill,name='history_purchasebill'),
    path('delete_purchasebill/<int:id>',views.delete_purchasebill,name='delete_purchasebill'), 
    path('history',views.history,name='history'),
    path('sharepdftomail/<int:id>',views.sharepdftomail,name="sharepdftomail"),
    path('import_purchase_bill',views.import_purchase_bill,name='import_purchase_bill'),
    path('billhistory',views.billhistory,name='billhistory'),
]

