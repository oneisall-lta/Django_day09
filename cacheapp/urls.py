from django.urls import path

from cacheapp import views

urlpatterns = [
    path('cake/<cake_id>/',views.get_cake),
    path('cakes/',views.my_view),
    path('all/',views.my_view)
]