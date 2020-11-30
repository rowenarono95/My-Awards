from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register,name = 'registration'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('search_results',views.search_results, name = 'search_results'),
    path('profile/', views.profile,name = 'profile'),
    path('new_project/', views.new_project,name ='new_project'),
    path('my_projects/', views.my_projects,name ='my_projects'),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)