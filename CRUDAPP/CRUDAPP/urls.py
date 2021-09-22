from django.contrib import admin
from django.urls import path
from enroll import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.addShow, name='addShow'),
    path('delete/<int:id>/', views.delete_data, name="deleteData")
    # path(' ',views.addShow, name="addShow")
]
