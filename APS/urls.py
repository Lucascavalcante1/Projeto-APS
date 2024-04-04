"""""
"""""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('to_do.urls')),
    path('', include('accounts.urls')),
    path('accounts/ ', include('django.contrib.auth.urls')),
    path('login/', LoginView.as_view(), name='login'),   
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
