from django.urls import path

from . import views

app_name = 'entries'
urlpatterns = [
    path('',views.AllView.as_view(),name='all'),
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('add/',views.AddView.as_view(),name='add'),
    path('update/<int:pk>',views.UpdateView.as_view(),name='update'),
    path('delete/<int:pk>',views.DeleteView.as_view(),name='delete'),
]
