"""estimation_in_earthquake_earlywarning URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Remote_User import views as remoteuser
from estimation_in_earthquake_earlywarning import settings
from Service_Provider import views as serviceprovider
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'^$', remoteuser.index, name="index"),
    path(r'^login/$', remoteuser.login, name="login"),
    path(r'^Register1/$', remoteuser.Register1, name="Register1"),
    path(r'^Predict_Earthquake_Early_Warning_Prediction/$', remoteuser.Predict_Earthquake_Early_Warning_Prediction, name="Predict_Earthquake_Early_Warning_Prediction"),
    path(r'^ViewYourProfile/$', remoteuser.ViewYourProfile, name="ViewYourProfile"),
    path(r'^serviceproviderlogin/$',serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    path(r'View_Remote_Users/$',serviceprovider.View_Remote_Users,name="View_Remote_Users"),
    path(r'^charts/(?P<chart_type>\w+)', serviceprovider.charts,name="charts"),
    path(r'^charts1/(?P<chart_type>\w+)', serviceprovider.charts1, name="charts1"),
    path(r'^likeschart/(?P<like_chart>\w+)', serviceprovider.likeschart, name="likeschart"),
    path(r'^View_Prediction_Of_Earthquake_Early_Warning_Ratio/$', serviceprovider.View_Prediction_Of_Earthquake_Early_Warning_Ratio, name="View_Prediction_Of_Earthquake_Early_Warning_Ratio"),
    path(r'^train_model/$', serviceprovider.train_model, name="train_model"),
    path(r'^View_Prediction_Of_Earthquake_Early_Warning/$', serviceprovider.View_Prediction_Of_Earthquake_Early_Warning, name="View_Prediction_Of_Earthquake_Early_Warning"),
    path(r'^Download_Trained_DataSets/$', serviceprovider.Download_Trained_DataSets, name="Download_Trained_DataSets"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
