from django.conf.urls import url, include
from django.contrib import admin
from main import views

urlpatterns = [
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^signup/', views.SignUpView.as_view(), name="signup"),
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^about/', views.AboutView.as_view(), name='about'),
    url(r'^photo/', views.PhotoView.as_view(), name='photo'),

]