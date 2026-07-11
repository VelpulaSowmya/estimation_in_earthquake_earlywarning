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
    path('', remoteuser.index, name="index"),
    path('login/', remoteuser.login, name="login"),
    path('Register1/', remoteuser.Register1, name="Register1"),
    path('Predict_Earthquake_Early_Warning_Prediction/', remoteuser.Predict_Earthquake_Early_Warning_Prediction, name="Predict_Earthquake_Early_Warning_Prediction"),
    path('ViewYourProfile/', remoteuser.ViewYourProfile, name="ViewYourProfile"),
    path('serviceproviderlogin/', serviceprovider.serviceproviderlogin, name="serviceproviderlogin"),
    path('View_Remote_Users/', serviceprovider.View_Remote_Users, name="View_Remote_Users"),
    path('charts/<str:chart_type>', serviceprovider.charts, name="charts"),
    path('charts1/<str:chart_type>', serviceprovider.charts1, name="charts1"),
    path('likeschart/<str:like_chart>', serviceprovider.likeschart, name="likeschart"),
    path('View_Prediction_Of_Earthquake_Early_Warning_Ratio/', serviceprovider.View_Prediction_Of_Earthquake_Early_Warning_Ratio, name="View_Prediction_Of_Earthquake_Early_Warning_Ratio"),
    path('train_model/', serviceprovider.train_model, name="train_model"),
    path('View_Prediction_Of_Earthquake_Early_Warning/', serviceprovider.View_Prediction_Of_Earthquake_Early_Warning, name="View_Prediction_Of_Earthquake_Early_Warning"),
    path('Download_Trained_DataSets/', serviceprovider.Download_Trained_DataSets, name="Download_Trained_DataSets"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
