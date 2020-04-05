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
    path('welcome/', portfolio.views.welcome),
    path('level2/', portfolio.views.leveltwo),
    path('final/', portfolio.views.final),
    path('hUghvIyiDyORYtgP/', portfolio.views.thanks),
    path('noyou/', portfolio.views.noyou),
    path('nome/', portfolio.views.nome),
    path('nono/', portfolio.views.nono),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)