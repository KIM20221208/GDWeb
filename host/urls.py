from django.urls import path

from host.views import listorders

# Router patterns: URLとcallされる関数のbind。
urlpatterns = [
    # My binds:
    path('orders/', listorders),

]
