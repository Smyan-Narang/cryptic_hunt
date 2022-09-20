"""cryptic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import include, re_path
from django.contrib import admin
from accounts.views import register, leaderboard, home, rules
from questions.views import Hunt
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
     re_path(r'^admin/', admin.site.urls),
     re_path(r'^register/$',register, name="register"),
     re_path(r'^leaderboard/$',leaderboard, name="leaderboard"),
     re_path(r'^hunt/$',Hunt.as_view(), name='hunt'),
     re_path(r'^login/$', auth_views.LoginView.as_view(
        redirect_authenticated_user=True, template_name = 'login.html'),
        name='login'),
     re_path(r'^logout/$', auth_views.LogoutView.as_view(template_name = 'home.html'),
        name='logout'),
     re_path(r'^$',home, name='home'),
     re_path(r'^rules/$',rules, name="rules")

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)