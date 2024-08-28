from django.urls import path
from.import views


urlpatterns = [
        path('',views.home),
        path('login/',views.userlogin,name="login"),
        path('userdashboard/',views.userdashboard,name="userdashboard"),
        path('newapplication/',views.newapplication,name="newapplication"),
        # path('viewapplication/',views.viewapplication,name="viewapplication"),
        # path('modifyapplication/',views.modifyapplication,name="modifyapplication")
    ]