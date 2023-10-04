from django.urls import path
from .views import PostRobotView

urlpatterns = [
    path('add/', PostRobotView.as_view(), name='add_robot'),

]
