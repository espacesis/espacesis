from django.conf import settings
from django.urls import include, path
from django.views.generic import TemplateView
from django.views import defaults as default_views

from .views import Softday9

app_name = "softday"


urlpatterns = [
    path("", Softday9.as_view(), name ="softday9"),
] 
