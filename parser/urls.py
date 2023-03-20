from django.contrib import admin
from django.urls import path

from pars_app.views import update, hi


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hi),
    path('update/', update)
]
