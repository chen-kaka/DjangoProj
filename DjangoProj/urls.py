"""DjangoProj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from DjangoProj.view import hello
from DjangoProj.testdb import testdb,testdbList,testdbUpdate,testdbDelete
from DjangoProj import search

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'hello/$', hello),
    url(r'^testdb/$', testdb),
    url(r'^testdb_list/$', testdbList),
    url(r'^testdb_update/$', testdbUpdate),
    url(r'^testdb_delete/$', testdbDelete),
    url(r'^search-form/$', search.search_form),
    url(r'^search/$', search.search),
    url(r'^search-post/$', search.search_post),
]
