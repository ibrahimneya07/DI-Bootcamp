from django.urls import path
from services.views import log_user, user_dashboard,base_page,graphiste,developpement,home,login,Details,index

urlpatterns = [
    path('home', home ,name='home'),

    path('graphiste', graphiste ,name='graphiste'),
    path('developpement', developpement ,name='developpement'),
    path('dashboard', user_dashboard, name='dashboard'),
    path('index', index, name='index'),
    path('Details/<int:user_id>', Details,name="Details"),

    
]