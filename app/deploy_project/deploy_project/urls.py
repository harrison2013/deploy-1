"""deploy_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from deploy_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello),
    path('db/', views.database),
    path('api/v1/<str:type>', views.list, name="list-items"),
    path('people/', views.people, name="list-people"),
    path('enterprises/', views.enterprises, name="list-enterprises"),
    path('governments/', views.governments, name="list-governments"),
    path('api/v1/<str:type>/<int:item_id>', views.item),
    path('api/v1/<str:type>/create', views.add_item),
    path('api/v1/<str:type>/<int:item_id>/delete', views.delete_item)
]
