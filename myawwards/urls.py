from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/register/', views.register, name='register'),
    path('search_results',views.search_results, name = 'search_results'),
    path('profile/', views.profile,name = 'profile'),
    path('new_project/', views.new_project,name ='new_project'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)