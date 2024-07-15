from django.contrib import admin
from django.urls import path
from core.views import homepage, product_detail, users_page, user_detail
from costumerapp.views import costumer_view
from news.views import news_view, news_detail

urlpatterns = [
    #general
    path('admin/', admin.site.urls),
    path('', homepage),
    #user
    path('users/', users_page, name='users'),
    path('users/user/<int:id>/', user_detail, name='user-profile'),
    #product
    path('product/<int:id>/', product_detail, name='product-detail'),
    #costumer
    path('costumers/', costumer_view),
    #news
    path('news/', news_view),
    path('news/<int:id>/', news_detail, name='news-detail'),
]
