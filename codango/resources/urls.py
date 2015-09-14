from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)create/$',
        views.Resources.as_view(),
        name='resource_create'),

    # url(r'^pdf/$',
    #     views.PdfResource.as_view(),
    #     name='pdf_create'),
]
