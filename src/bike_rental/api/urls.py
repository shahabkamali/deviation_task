from django.conf.urls import url


from . import views

urlpatterns = [

    url(r'^deviation/$',
        views.GetDeviationAPIView.as_view(),
        name='deviation'),

]
