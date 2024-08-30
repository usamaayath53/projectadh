from django.urls import path
from.import views


urlpatterns = [
        path('',views.home),
        path('login/',views.userlogin,name="login"),
        path('userdashboard/',views.userdashboard,name="userdashboard"),
        path('newapplication/',views.newapplication,name="newapplication"),
        path('view/',views.viewapplication,name="viewapplication"),
        path('search/',views.search, name="search"),
        path('editview/search/',views.editview,name="editview"),
        path('editview/',views.editview,name="editview"),
        path('editapp/<pk>',views.editapp,name='editapp'),
        path('view/search/',views.editsearch,name="editsearch"),
        path('links/',views.quicklinks,name="quicklinks"),
        path('logout/',views.userlogout,name='logout')
        # path('search/editapp/<pk>',views.editapp, name="searchedit"),
        
    ]