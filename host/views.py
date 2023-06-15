from django.shortcuts import render
from django.http import HttpResponse

from common.models import Customer


# Create your views here.
def listorders(request):
    return HttpResponse("下面是系统中所有的订单信息。。。二级表接口实现")


#
def listcustomers(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    # 每条表记录都是是一个dict对象，
    # key 是字段名，value 是 字段值
    qs = Customer.objects.values()

    # 定义返回字符串
    retStr = str()
    for customer in qs:
        for name, value in customer.items():
            retStr += f'{name} : {value} | '

        # <br> 表示换行
        retStr += '<br>'

    return HttpResponse(retStr)


#
def listcustomerByPhoneNum(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Customer.objects.values()

    # 检查url中是否有参数phonenumber
    ph = request.GET.get('phoneNumber', None)

    # 如果有，添加过滤条件
    if ph:
        qs = qs.filter(phoneNumber=ph)

    # 定义返回字符串
    retStr = str()
    for customer in qs:
        for name, value in customer.items():
            retStr += f'{name} : {value} | '
        # <br> 表示换行
        retStr += '<br>'

    return HttpResponse(retStr)
