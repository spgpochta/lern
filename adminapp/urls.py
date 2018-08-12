from django.conf.urls import url
import adminapp.views as adminapp
from django.urls import path

app_name = 'admin'

urlpatterns = [
    url(r'^users/create/$', adminapp.user_create, name='user_create'),
    url(r'^users/read/$', adminapp.UserListView.as_view(), name='users'),
    url(r'^users/update/(?P<pk>\d+)/$', adminapp.user_update,
        name='user_update'),
    url(r'^users/delete/(?P<pk>\d+)/$', adminapp.user_delete,
        name='user_delete'),
    # path('users/update/password/<int:pk>/', adminapp.password_change,
    #     name='user_update'),

    url(r'^categories/create/$', adminapp.CategoryCreateView.as_view(),
        name='category_create'),
    # url(r'^categories/read/$', adminapp.CategoryListView.as_view(),
    #     name='categories'),
    url(r'^categories/read/$', adminapp.categories, name='categories'),
    url(r'^categories/update/(?P<pk>\d+)/$',
        adminapp.CategoryUpdateView.as_view(), name='category_update'),
    url(r'^categories/delete/(?P<pk>\d+)/$',
        adminapp.CategoryDeleteView.as_view(), name='category_delete'),

    url(r'^products/create/category/(?P<pk>\d+)/$',
        adminapp.product_create, name='product_create'),
    # url(r'^products/read/category/(?P<pk>\d+)/$', adminapp.products,
    #     name='products'),
    path('products/read/<int:pk>/', adminapp.products,
         name='products'),
    url(r'^products/read/(?P<pk>\d+)/$', adminapp.products,
        name='product_read'),
    url(r'^products/update/(?P<pk>\d+)/$', adminapp.product_update,
        name='product_update'),
    url(r'^products/delete/(?P<pk>\d+)/$', adminapp.product_delete,
        name='product_delete'),

    path('contacts/read/', adminapp.ContactsListlView.as_view(),
         name='contacts'),
]

# urlpatterns += patterns('django.contrib.auth.views',
#   url(r'^user/(?P<user_id>\d+)/user_edit/password/$', 'password_change')
# )
