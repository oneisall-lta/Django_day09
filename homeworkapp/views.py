from django.core.cache import cache
from django.shortcuts import render

# Create your views here.
from homeworkapp.models import Student


def gostudent(req):
    return render(req, 'students.html')


def getallstudents(request):
    value = cache.get('all')  # 尝试从缓存中获取学生信息
    if value:
        return render(request, 'students.html', {'students': value, 'msg': '恭喜，缓存命中了！'})
    else:
        students = Student.objects.all()
        cache.set('all', students, 60)  # 数据放入缓存，并设置缓存时间
        return render(request, 'students.html', {'students': students, 'msg': '从数据库中查到的学生信息……'})
