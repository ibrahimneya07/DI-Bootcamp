from django.urls import path
from comptes import views 

urlpatterns = [
    path('',views.login_page, name='login'),
    path('logout', views.logout_user,name='logout'),
    path('signUp',views.signup_page, name='signUp'),    
    path('discussion/<int:user_id>',views.discussion, name='Discussion'),
    path('mes/<int:user_id>',views.mes, name='mes'),

    # path('profile/<int:id>',views.profile,name='profile'),


  ]