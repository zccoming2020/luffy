
# 一定要在settings文件中将异常模块配置自己的异常处理函数
from rest_framework.response import Response
from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework import status
from .logging import logger

def exception_handler(exc,context):
    response = drf_exception_handler(exc,context)
    detail = '%s-%s-%s' % (context.get('view'), context.get('request').method, exc)
    if not response: # 服务器端错误

       response =  Response({'detail':detail}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
       response.data = {'detail':detail}

    # 核心：要将response.data.get('detail)信息记录到日志文件
    logger.warning(response.data.get('detail'))

    # print(response.data.get('detail'))
   # < api.views.BookAPIViewsobjectat0x000000000B9FA3C8 > -PUT - 方法 “PUT” 不被允许。

    # import sys
    # sys.stderr.write('异常：%s\n' % response.data.get('detail'))
    # return response

