from django.shortcuts import render,HttpResponse,redirect,reverse
from user.models import *
# Create your views here.
from django.views import View
# 导入正则
import re


# 发送验证码模型类
from ronglian_sms_sdk import SmsSDK
class Sent_Mess(View):
    def get(self,request):
        # accId = '容联云通讯分配的主账号ID'
        # accToken = '容联云通讯分配的主账号TOKEN'
        # appId = '容联云通讯分配的应用ID
        accId ='8a216da87c304531017c6a4cebe50718'
        accToken ='9d9886d1765643a392e81261601d27a3'
        appId ='8aaf07087ce03b67017cfffd55750718'
        #初始化 SDK
        sdk = SmsSDK(accId,accToken,appId)
        # 配置要发送的验证码的模板型号，手机号(最多200), datas(变量)
        tid = '1'
        mobile = '13762711904,15773998780'
        # 验证码是5426,请于3分钟正常输入
        datas = ('5426','3')
        # 发送验证码
        resp = sdk.sendMessage(tid,mobile,datas)
        print(resp)
        return HttpResponse("发送成功")


from django.contrib.auth import logout,login
class LoginView(View):
    def get(self,request):
        logout(request)
        return render(request,'login.html')
    def post(self,request):
        name = request.POST.get('username')
        password = request.POST.get('password')
        if not name:
            return HttpResponse("请输入用户名")
        if not re.match(r'^[0-9a-zA-Z]{8,20}$',password):
            return HttpResponse("密码错误")
        try:
            user = BlogUser.objects.get(username=name)
        except :
            return HttpResponse("用户名或密码错误")
        next_page = request.GET.get('next')
        if next_page == '/detail/':
            resp =  redirect(reverse('blogapp:detail'))
        elif next_page == '/list/':
            resp =  redirect(reverse('blogapp:list'))
        else:
            resp = redirect(reverse("blogapp:index"))
        login(request, user)
        return resp
class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        username=request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        if not re.match(r'^[0-9a-zA-Z]{8,20}$',password):
            return HttpResponse('请安规定输入密码，请输入8-20位密码的账户')
        try:
            user = BlogUser()
            user.password = password
            user.email = email
            user.username = username
            user.save()
        except Exception as e :
            print(e)
            return HttpResponse("注册失败")
        return redirect(reverse('blogapp:index'))