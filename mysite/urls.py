"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from popular import views
from django.contrib.auth import views as auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='home'),
    url(r'^govtadmin',auth.login,{'template_name': 'govtadminlogin.html'},name='govtadminlogin'),
    url(r'^govtpage',views.govt,name="govt"),
    url(r'^about',views.about,name="about"),
    url(r'^contact',views.contact,name="contact"),
    url(r'^charts/$',views.chart,name='chart'),
    url(r'^new_customer/$',views.new_customer,name='new_customer'),
    url(r'^login/$', auth.login, {'template_name': 'login.html'},name='login'),
    url(r'^logout/$', auth.logout, name='logout'),
    url(r'^users/change_password/$', login_required(auth.password_change), {'post_change_redirect' : '/','template_name': 'change_password.html'}, name='change_password'),

    # Links for Hotel
    url(r'^all_hotel_name',views.all_hotel_name,name="all_hotel_name"),
    # Link for National-parks
    url(r'^all_national_park_name',views.all_national_park_name,name="all_national_park_name"),
    # Link for Lake
    url(r'^all_lake_name',views.all_lake_name,name="all_lake_name"),
    # Link for Temple
    url(r'^all_temple_name',views.all_temple_name,name="all_temple_name"),

    #Link for Hotel-1 Data
    url(r'^hotel1_data',views.hotel1_data,name="hotel1.data"),

    url(r'^approve_data_hotel1',views.approve_data_hotel1,name="approve_data_hotel1"),
    #Link for National-Park-1 Data 
    url(r'^national_park1_data',views.National_Park1_data,name="National_Park1.data"),
    #Link for Hotel-1 Data 
    url(r'^approve_data_national_park1',views.approve_data_National_Park1,name="approve_data_National_Park1"),

    #Link for National-Park-1 Data 
    url(r'^lake1_data',views.Lake1_data,name="Lake1.data"),
    #Link for Hotel-1 Data 
    url(r'^approve_data_lake1',views.approve_data_Lake1,name="approve_data_Lake1"),

    #Link for National-Park-1 Data 
    url(r'^temple1_data',views.Temple1_data,name="Temple1_data"),
    #Link for Hotel-1 Data 
    url(r'^approve_data_temple1',views.approve_data_Temple1,name="approve_data_Temple1"),



    # Final Website
    url(r'^overall',views.overall,name="overall"),

    # All Hotel-name
    url(r'^hotel_list',views.hotel_list,name="hotel_list"), 

    #Permit office
    url(r'^permit_office',views.permit_office,name="permit_office"), 

    # Tourist Destination
    url(r'^destination',views.destination,name="destination"),

    #All National Park
     #url(r'^national_park',views.national_park,name="national_park"), 

    #All Museums
    #All National Park
     #url(r'^museums',views.museums,name="museums"), 

    # List of national parks
    url(r'^np_list',views.np_list,name="np_list"), 
    # List of national parks
    url(r'^museums',views.museums,name="museums"), 
    # List of monestry
    #url(r'^monestry',views.monestry,name="monestry"), 

     #Hotel_Anlaysis_2017
     url(r'^hotel_analysis_2017', views.hotel_analysis_2017,name="hotel_analysis_2017"),
     #Hotel_Anlaysis_2016
     url(r'^hotel_analysis_2016', views.hotel_analysis_2016,name="hotel_analysis_2016"),
     #Hotel_Anlaysis_2015
     url(r'^hotel_analysis_2015', views.hotel_analysis_2015,name="hotel_analysis_2015"),
     #Hotel_Anlaysis_2014
     url(r'^hotel_analysis_2014', views.hotel_analysis_2014,name="hotel_analysis_2014"),
     #Hotel_Anlaysis_2013
     url(r'^hotel_analysis_2013', views.hotel_analysis_2013,name="hotel_analysis_2013"),
     #Hotel_Anlaysis_2012
     url(r'^hotel_analysis_2012', views.hotel_analysis_2012,name="hotel_analysis_2012"),
     #Hotel_Anlaysis_2011
     url(r'^hotel_analysis_2011', views.hotel_analysis_2011,name="hotel_analysis_2011"),

     #Monthly Data Overall
     url(r'^hotel_analysis_jan', views.hotel_analysis_jan,name="hotel_analysis_jan"),
     url(r'^hotel_analysis_feb', views.hotel_analysis_feb,name="hotel_analysis_feb"),
     url(r'^hotel_analysis_mar', views.hotel_analysis_mar,name="hotel_analysis_mar"),
     url(r'^hotel_analysis_apr', views.hotel_analysis_apr,name="hotel_analysis_apr"),
     url(r'^hotel_analysis_may', views.hotel_analysis_may,name="hotel_analysis_may"),
     url(r'^hotel_analysis_jun', views.hotel_analysis_jun,name="hotel_analysis_jun"),
     url(r'^hotel_analysis_july', views.hotel_analysis_july,name="hotel_analysis_july"),
     url(r'^hotel_analysis_aug', views.hotel_analysis_aug,name="hotel_analysis_aug"),
     url(r'^hotel_analysis_sep', views.hotel_analysis_sep,name="hotel_analysis_sep"),
     url(r'^hotel_analysis_oct', views.hotel_analysis_oct,name="hotel_analysis_oct"),
     url(r'^hotel_analysis_nov', views.hotel_analysis_nov,name="hotel_analysis_nov"),
     url(r'^hotel_analysis_dec', views.hotel_analysis_dec,name="hotel_analysis_dec"),









     #National Park Analysis
     
 















































]

