from django.urls import path
from .views import PostRobotView, index, export_to_excel

urlpatterns = [
    path('', index),
    path('add/', PostRobotView.as_view(), name='add_robot'),
    path('excel/', export_to_excel, name='save_excel')
]
