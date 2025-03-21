"""shoppingmall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.homepage, name='homepage'),  # 首页：产品类型
    path('products/<int:type_id>/', views.product_list, name='product_list'),  # 次页：产品列表
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),  # 次页：产品详情

    path('search/', views.search_results, name='search_results'),
    
]
#+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#https://render.com/docs/deploy-django?_gl=1*7io44p*_gcl_au*MTExMjkxODU2OS4xNzQyNDU5NTM5*_ga*MTU0MDE5NDgzMy4xNzQyNDM1NTA3*_ga_QK9L9QJC5N*MTc0MjQ1OTUzOC4yLjEuMTc0MjQ2MjE0My40MS4wLjA.#static-files
