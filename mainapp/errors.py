from rest_framework.exceptions import APIException


class SSSException(APIException):   #  自定义异常类
    def __init__(self,detail):
        self.detail = detail   # 将异常的详细信息封装到detail实例属性中