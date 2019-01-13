from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from views import FragmentListView

from . import views
appname = 'hereditatem'
urlpatterns = [
    url(r'^$' , views.index, name='index'),
    url(r'^panels/$',views.panels, name="tile-panels"),
    url(r'^fragments/$', FragmentListView.as_view(), name='fragments'),
    url(r'^fragment/([0-9]*)$', views.fragment, name='fragment-details'),
    #url(r'^fragment/', views.fragment, name='add-fragment'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)