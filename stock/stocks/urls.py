from django.conf.urls import url
from .views import GetKlinesView, GetAllListView, GetIndustryView,GetARBRView

urlpatterns = [
    url(r'klines/',GetKlinesView,name='klines'),
    url(r'allstock/',GetAllListView,name='allstock'),
    url(r'industrydata/',GetIndustryView,name='industrydata'),
    url(r'arbr/',GetARBRView,name='industrydata'),
]
