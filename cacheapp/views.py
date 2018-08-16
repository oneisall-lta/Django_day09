from django.core.cache import cache
from django.shortcuts import render

# Create your views here.
from django.views.decorators.cache import cache_page

from cacheapp.models import Cake


def get_cake(req, cake_id):
    value = cache.get('cake_' + cake_id)  # 使用底层cache API尝试获取缓存中的数据
    if value:
        return render(req, 'cake.html', {'cake': value, 'msg': '恭喜，缓存命中了！'})
    else:
        cake = Cake.objects.get(id=cake_id)  # 查询mysql数据库内容
        cache.set('cake_' + cake_id, cake, 30)  # 设置缓存
        return render(req, 'cake.html', {'cake': cake, 'msg': '从mysql数据库中查到的数据……'})


count = 0


@cache_page(30)  # 设置视图缓存结果的时间，30秒内只能调用一次,不同的路径访问同一个my_view视图，独立缓存结果，互不影响。
def my_view(request):
    global count
    count += 1
    print('第' + str(count) + '次调用my_view函数')
    cakes = Cake.objects.all()
    return render(request, 'cakes.html', {'cakes': cakes, 'msg': '第' + str(count) + '次调用my_view函数'})
