from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

import portfolio.views 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', portfolio.views.preload),
    path('portfolio', portfolio.views.index),
    path('brunyrus', portfolio.views.brunyrus),
    path('brunylex', portfolio.views.answer),
    path('report', portfolio.views.report),
    path('thanks', portfolio.views.thanks),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)