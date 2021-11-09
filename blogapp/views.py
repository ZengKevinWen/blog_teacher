import random

from django.core.paginator import Paginator
from django.shortcuts import render,redirect,reverse,HttpResponse
from django.views import View
from blogapp.models import *
from django.contrib.auth.mixins import LoginRequiredMixin


def test(request):
    return render(request,'test.html')
#首页类型
class IndexView(View):
    def get(self,request):
        # 所有博客与实现搜索功能
        search_post = request.GET.get('search')
        post_list = Post.objects.all()
        # 判断是否进行搜索功能实现 如果是展示搜索的博客 不是则显示所有博客
        if  search_post:
            post_list = Post.objects.filter(category_id=search_post)
        # 获取页面参数
        page_id = request.GET.get('page',1)
        # 创建分页器  对数据进行分页
        post_Paginator = Paginator(post_list,1)
        # 获取分页器中某一页的数据  id=那一页
        page_data = post_Paginator.page(page_id)
        # 推荐博客 -------------------对于BooleanField类型的数据来说输出的是True/false类型所以在filter判断时要写True或者False
        recommend_post_list = Post.objects.filter(recommend=True)
        # 友情链接
        friendlylink_list = FriendlyLink.objects.all()
        # 轮播图
        banner_list = Banner.objects.all()
        # 最新博客评论 ------------------------技术不到位   搞的自己有点小麻烦
        comment_list1 = Comment.objects.all().values('post_id')
        pid=[]
        print(comment_list1)
        for c in comment_list1:
            if c['post_id'] not in pid:
                pid.append(c['post_id'])
        comment_list = []
        for a in pid:
            m = Comment.objects.filter(post_id=a).order_by('-id')[0]
            comment_list.append(m)
        # 博客分类
        post_cagetory_list = BlogCategory.objects.all().order_by('-id')[:6]
        context = {
            'page_data':page_data,
            'friendlylink_list':friendlylink_list,
            'banner_list':banner_list,
            'comment_list':comment_list,
            'post_category_list':post_cagetory_list,
            'recommend_post_list':recommend_post_list,
            'post_Paginator':post_Paginator,
        }
        print(page_data)
        return render(request,'index.html',context=context)
    # 为搜索功能准备的
    def post(self,request):
        blog_category_search = request.POST.get("category")
        # 在前段传值不知道为什么失败，等待问老师！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
        print(blog_category_search)
        # 调用django自带的模糊查询方式 (item_info_icontains = 模糊查询的字段).all()----列表类型   item_info(表示在表中的那个字段进行模糊查询)---------------------有个很大的缺点(只能够过不区分大小写的模糊匹配(双下划线))
        blog_category = BlogCategory.objects.filter(name__icontains=blog_category_search).all()
        #  对象中的数据 ！！！！！！ 请注意容易出错
        if not blog_category[0] :
            return HttpResponse("请输入正确关键字")
        # return render(request, 'index.html', context=context)
        return redirect('/index/?search=%s'%blog_category[0].id)
        # for blog_title in BlogCategory.objects.all():
        #     if blog_title.name == blog_category_search:
        #         pass
# 列表页面类
class ListView(LoginRequiredMixin,View):
    def get(self,request):
        post_list = Post.objects.all().order_by('-id')
        # 最新博客评论 ------------------------技术不到位   搞的自己有点小麻烦
        comment_list1 = Comment.objects.all().values('post_id')
        pid = []
        print(comment_list1)
        for c in comment_list1:
            if c['post_id'] not in pid:
                pid.append(c['post_id'])
        comment_list = []
        for a in pid:
            m = Comment.objects.filter(post_id=a).order_by('-id')[0]
            comment_list.append(m)
        # 标签
        tags_list = Tags.objects.all()
        context = {
            'post_list':post_list,
            'news_comment_list':comment_list,
            'tags_list':tags_list,
        }
        return render(request,'list.html',context=context)

# 详细页面类
class DetailView(LoginRequiredMixin,View):
    def get(self,request):
        #详细页面
        post_detail_id = request.GET.get('id',1)
        post_detail = Post.objects.get(id=post_detail_id)
        # 相关推荐
        friendlylink_list = FriendlyLink.objects.all().order_by('-id')[:4]
        # 标签
        tags_list = Tags.objects.all()
        # 最新博客评论 ------------------------技术不到位   搞的自己有点小麻烦
        comment_list1 = Comment.objects.all().values('post_id')
        pid = []
        print(comment_list1)
        for c in comment_list1:
            if c['post_id'] not in pid:
                pid.append(c['post_id'])
        comment_list = []
        for a in pid:
            m = Comment.objects.filter(post_id=a).order_by('-id')[0]
            comment_list.append(m)
        context = {
            'friendlylink_list':friendlylink_list,
            'post_detail':post_detail,
            'tags_list':tags_list,
            'new_comment_list':comment_list,
        }
        return render(request,'show.html',context=context)

    def post(self,request):
        comment_name = 1
        request_dict =request.POST
        comment_text = request_dict.get('content')
        comment_post_id =request_dict.get('id')  # 不知道为什么一直没有传值传过来
        try:
            comment = Comment()
            comment.content = comment_text
            comment.user_id = comment_name
            comment.post_id = int(comment_post_id)
            comment.save()
        except Exception as e:
            print(e)
            return HttpResponse("评论失败:%s"%e)
        return redirect('/detail/?id=%s'%comment_post_id)

# 404页面类
class Test_404View(View):
    def get(self,request):
        pass
        return render(request,'404.html')
