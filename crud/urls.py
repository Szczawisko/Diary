from django.urls import path

from . import views

app_name = 'entries'
urlpatterns = [
    path('',views.DiaryListApiView.as_view()),
    path('/<int:id>',views.DiaryDetailApiView.as_view()),
]
