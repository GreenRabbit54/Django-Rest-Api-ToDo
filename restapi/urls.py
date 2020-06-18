
from django.contrib import admin
from django.urls import path
from restpolls.apiviews import PollList, PollDetail,ChoiceList, CreateVote
from restpolls.views import polls_list, polls_detail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', PollList.as_view(), name='polls_list'),
    path('polls/<int:pk>/',PollDetail.as_view(), name = 'polls_detail'),
    path('polls/<int:pk>/choices/',ChoiceList.as_view(),name = "choice_list"),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/',CreateVote.as_view(), name = 'create_vote'),
]
