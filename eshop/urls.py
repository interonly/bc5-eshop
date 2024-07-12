from django.contrib import admin
from django.urls import path
from core.views import homepage, product_detail
from costumerapp.views import costumer_view
from news.views import news_view, news_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('product/<int:id>/', product_detail, name='product-detail'),
    path('costumers/', costumer_view),
    path('news/', news_view),
    path('news/<int:id>/', news_detail, name='news-detail'),
]
