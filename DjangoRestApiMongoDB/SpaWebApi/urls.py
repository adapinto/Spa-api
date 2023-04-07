from django.urls import re_path
from SpaWebApi.CitaTipoTratamiento.view import citaTipoTratamiento_list




urlpatterns = [
     re_path(r'^api/citaTipoTratamiento$', citaTipoTratamiento_list )
]