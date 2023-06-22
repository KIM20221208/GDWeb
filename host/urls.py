from django.urls import path

from host import views

# Router patterns: URLとcallされる関数のbind。
urlpatterns = [
    # My binds:
    path('orders/', views.listorders),
    path('customers/', views.listcustomers),
    path('customerByPhoneNum/', views.listcustomerByPhoneNum),
    # path('crawlSteamUserBySteamID/', views.list_user_by_steam_id),

]
