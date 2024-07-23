from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import homepage, search, product_detail, product_create, users_page, user_detail
from costumerapp.views import costumer_view, costumer_create, profile_view, profile_detail, profile_create
from news.views import news_view, news_detail, new_create

urlpatterns = [
    #general
    path('admin/', admin.site.urls),
    path('', homepage),
    path('search/', search),

    #user
    path('users/', users_page, name='users'),
    path('users/user/<int:id>/', user_detail, name='user-profile'),

    #product
    path('product/<int:id>/', product_detail, name='product-detail'),
    path('product-create/', product_create, name='product-create'),

    #costumer
    path('costumers/', costumer_view, name='costumers'),
    path('costumer-create/', costumer_create, name='costumer-create'),
    
    #profile
    path('profiles', profile_view, name ='profiles'),
    path('profile/<int:id>/', profile_detail, name='profile-detail'),
    path('profile-create/', profile_create, name ='profile-create'),

    #news
    path('news/', news_view, name='news'),
    path('news/<int:id>/', news_detail, name='news-detail'),
    path('new-create/', new_create, name='new-create'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
