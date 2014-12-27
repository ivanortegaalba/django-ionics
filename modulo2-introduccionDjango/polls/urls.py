from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('',
    url(r'^$',views.index, name='index'),
    url(r'^(?P<questionId>\d+)/$',views.details, name='details'),
    url(r'^(?P<questionId>\d+)/results/$',views.results, name='results'),
    url(r'^(?P<questionId>\d+)/vote/$',views.vote, name='vote')

)
