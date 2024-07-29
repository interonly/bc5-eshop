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
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('product-create/', ProductCreateView.as_view(), name='product-create'),
    path('product-update/<int:id>/', product_update, name='product-update'),

    #costumer
    path('costumers/', costumer_view, name='costumers'),
    path('costumer-create/', costumer_create, name='costumer-create'),
    
    #profile/user
    path('users/', users_list, name='users'),
    path('user/<int:id>/', user_cabinet, name='user-cabinet'), 
    path('profile-create/', ProfileCreateView.as_view(), name ='profile-create'),
    path('profile-update/<int:id>/', profile_update, name='profile-update'),

    #news
    path('news/', news_view, name='news'),
    path('new/<int:pk>/', NewDetailView.as_view(), name='news-detail'),
    path('new-create/', NewCreateView.as_view(), name='new-create'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
