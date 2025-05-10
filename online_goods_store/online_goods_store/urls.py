"""
URL configuration for online_goods_store project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import app.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.views.home, name='home'),
    path('catalog/', app.views.catalog, name='catalog'),
    path('product/', app.views.product, name='product'),
    path('order_placing/', app.views.order_placing, name='order_placing'),
    path('authorization/', app.views.authorization, name='authorization'),
    path('registration/', app.views.registration, name='registration'),
    path('authorization/output_password/', app.views.output_password, name='output_password'),
    path('reporting/', app.views.reporting, name='reporting'),
    path('personal_account/', app.views.personal_account, name='personal_account'),
    path('add_product/', app.views.add_product, name='add_product'),
    path('change_product/', app.views.change_product, name='change_product'),
    path('qwe/', app.views.qwe, name='qwe'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
