from django.urls import path

from host.views import listorders
from host.views import listcustomers
from host.views import listcustomerByPhoneNum

# Router patterns: URLとcallされる関数のbind。
urlpatterns = [
    # My binds:
    path('orders/', listorders),
    path('customers/', listcustomers),
    path('customerByPhoneNum/', listcustomerByPhoneNum),

]
