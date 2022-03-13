from django.contrib import admin
from django.conf.urls import re_path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from . import views
from django.conf import settings
from categories.views import CategoriesView, CategoryCreate, CategoryDelete, CategoryUpdate
from products.views import ProductView, ProductCreate, ProductUpdate, ProductDelete
from publicProducts.views import PublicProductView

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'login/$', views.login_view, name="login"),
    re_path(r'logout/$', views.logout_view, name="logout"),
    re_path(r'^categories/$', CategoriesView.as_view(), name='categories_list'),
    re_path(r'^categories/create$', CategoryCreate.as_view(), name='category_create'),
    re_path(r'^categories/edit/(?P<pk>\d+)$', CategoryUpdate.as_view(), name='category_edit'),
    re_path(r'^categories/delete/(?P<pk>\d+)$', CategoryDelete.as_view(), name='category_delete'),
    
    re_path(r'^products/$', ProductView.as_view(), name='products_list'),
    re_path(r'^products/create$', ProductCreate.as_view(), name='product_create'),
    re_path(r'^products/edit/(?P<pk>\d+)$', ProductUpdate.as_view(), name='product_edit'),
    re_path(r'^products/delete/(?P<pk>\d+)$', ProductDelete.as_view(), name='product_delete'),

    re_path(r'^public/$', PublicProductView.as_view(), name="public_store"),
    re_path(r'^$', views.homepage, name="homepage"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
