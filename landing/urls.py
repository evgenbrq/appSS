from django.urls import path
from landing import views

urlpatterns = [
    path('', views.index, name='new_application'),
    path('about', views.about, name='about'),
    path('about/<int:pk>', views.ApplicationDetailView.as_view(), name='application-detail'),
    path('about/<int:pk>/update', views.ApplicationUpdateView.as_view(), name='application-update'),
    path('about/<int:pk>/delete', views.ApplicationDeleteView.as_view(), name='application-delete'),
    path('application', views.application, name='application'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('report', views.Report.as_view(), name='report'),
    path('export_excel', views.export_excel, name='export_excel'),
]