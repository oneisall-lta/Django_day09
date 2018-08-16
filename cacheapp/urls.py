from django.urls import path

from cacheapp.views import *

urlpatterns = [
    path('cake/<cake_id>/', get_cake),
    path('cakes/', my_view),
    path('all/', my_view),
    path('allcake/', cache_page(60 * 15)(cake_views)),
]
