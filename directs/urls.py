from directs.views import inbox, Directs, SendDirect, UserSearch, NewConversation, tag_search
from django.urls import path

urlpatterns = [
    path('', inbox, name="message"),
    path('direct/<username>', Directs, name="directs"),
    path('send/', SendDirect, name="send-directs"),
    path('search/', UserSearch, name="search-users"),
    path('tag_search/', tag_search, name="tag_search"),
    path('new/<username>', NewConversation, name="conversation"),
]