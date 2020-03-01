from django.contrib import admin
from django.urls import path

import portfolio.views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolio.views.index)
]