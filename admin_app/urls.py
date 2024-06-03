from django.urls import path
from .import views
urlpatterns = [
    path('', views.userlist_appointment, name='userlist_appointment'),
    path('user_details/<int:appointment_id>', views.userdetails_appointment, name='user_details'),
path('user_update/<int:appointment_id>/', views.user_update_appointment, name='user_update'),
path('user_create', views.user_book_appointment, name='user_create'),
path('user_delete/<int:appointment_id>/', views.deleteView, name='user_delete'),
    path('userlist/', views.userlist, name='userlist'),


path('facility_delete/<int:facilities_id>/', views.facility_delete, name='facility_delete'),
path('facility_details/<int:facilities_id>/', views.facility_details, name='facility_details'),
path('facility_update/<int:facilities_id>/', views.facility_update, name='facility_update'),
path('facility_create/', views.facility_create, name='facility_create'),


path('details_user/<int:users_id>/',views.user_detail,name='details_user'),
path('delete_user/<int:users_id>/',views.user_deleteView,name='delete_user'),






]