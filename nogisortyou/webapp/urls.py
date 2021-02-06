from django.urls import path
from webapp.views import (index_view,
                          login_view,
                          test_view)

urlpatterns = [
    path('', index_view),
    path('login/', login_view),
    path('unco/', test_view)
]
