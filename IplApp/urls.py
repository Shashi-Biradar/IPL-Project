from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('info/',views.info,name='info'),
    path('create/',views.create_franchise,name='create_franchise'),
    path('update-franchise/<int:id>',views.update_franchise,name='update_franchise'),
    path('list-franchise/',views.list_franchise,name='list_franchise'),
    path('franchise-details/<int:id>',views.franchise_details,name='franchise_details'),
    path('delete-franchise/<int:id>',views.delete_franchise,name='delete_franchise'),
    path('create-player/',views.create_player,name='create_player'),
    path('list-players/<int:franchise_id>',views.list_players,name='list_players'),
    path('create-stadium/',views.create_stadium,name='create_stadium'),
    path('list-stadiums/',views.list_stadiums,name='list_stadiums'),
    path('register-user/',views.register_user,name='register_user'),
    path('',views.login_user,name='login_user'),


]