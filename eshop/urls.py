from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core.views import *
from costumerapp.views import *
from news.views import *
urlpatterns = [
    #general
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('search/', search),
    path('registration/', registration, name='registration'),
    path('signin/', signin, name='signin'),
    path('signout/', signout, name='signout'),

    #product
    path('product/<int:id>/', product_detail, name='product-detail'),
    path('product-create/', product_create, name='product-create'),
    path('product-update/<int:id>/', product_update, name='product-update'),

    #costumer
    path('costumers/', costumer_view, name='costumers'),
    path('costumer-create/', costumer_create, name='costumer-create'),
    
    #profile/user
    path('users/', users_list, name='users'),
    path('user/<int:id>/', user_cabinet, name='user-cabinet'), 
    path('profile-create/', profile_create, name ='profile-create'),
    path('profile-update/<int:id>/', profile_update, name='profile-update'),

    #news
    path('news/', news_view, name='news'),
    path('news/<int:id>/', news_detail, name='news-detail'),
    path('new-create/', new_create, name='new-create'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
