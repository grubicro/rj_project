from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^about/$',views.AboutView.as_view(),name='about'),
    url(r'^pregled/$', views.GJList.as_view(), name='gj_list'),
    url(r'^create/$', views.CreateGJ.as_view(), name='create_gj'),
    url(r'^edit/(?P<pk>\d+)/$', views.EditGJ.as_view(), name='edit_gj'),
    url(r'^delete/(?P<pk>\d+)/$', views.DeleteGJ.as_view(), name='delete_gj'),
]
