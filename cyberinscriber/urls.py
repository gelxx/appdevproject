from django.urls import path
from . import views
from cyberinscriber import views as user_views



#paths arranged alphabetically by name
app_name = 'cyberinscriber'
urlpatterns = [ 
#URLs for inventory app

      #path('admin/', admin.site.urls),


      path('landingpage', views.LandingView, name="landingpage_view"),
      path('register',views.register, name="register_view"),
      path('login',views.loginPage,name="login_view"),
      path('logout',views.logOutUser,name ="logout_view"),
      path('myhome',views.MyHomeView, name="myhome_view"),



   ]