from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static
from . import view
 
urlpatterns = [
    url(r'^$', view.index),
]  + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

