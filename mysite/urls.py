from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

import portfolio.views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolio.views.redirect_to_index),
    path('portfolio/', portfolio.views.index),
    path('whoami/', portfolio.views.whoami),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)