
from django.db import models


from django.utils import timezone

# 轮播图模型类
class Banner(models.Model):
    title = models.CharField(max_length=50,verbose_name='标题')
    cover = models.ImageField(upload_to='static/images/banner',verbose_name='轮播图')
    # 图片链接url类型 -------------之前没有用过注意！！！！！！！！！！
    link_url = models.URLField(verbose_name='图片链接',max_length=100)
    # 数值数据类型
    idx = models.IntegerField(verbose_name='索引')
    # 布尔类型  用的少多注意!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    is_active = models.BooleanField(verbose_name="是否活跃",default=False)
    str1 = models.CharField(max_length=20,blank=True)
    def __str__(self):
        return self.title
    class Meta:
        db_table='blog_db_banner'
        verbose_name = "轮播图"
        verbose_name_plural=verbose_name

# 博客分类
class BlogCategory(models.Model):
    name = models.CharField(max_length=20,verbose_name="博客分类名称")
    str1 = models.CharField(max_length=20,blank=True)
    class Meta:
        db_table = "blog_db_blogcategory"
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

#Tags---标签模型类
class Tags(models.Model):
    name = models.CharField(max_length=20,verbose_name='标签名称',default='')
    str1 = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'blog_db_tags'
        verbose_name = 'Tags标签'
        verbose_name_plural= verbose_name
# 友情链接模型类
class FriendlyLink(models.Model):
    title = models.CharField(max_length=50,verbose_name='标题')
    # URL类型
    link = models.URLField(max_length=50,default='',verbose_name='友情链接')
    str1 = models.CharField(max_length=20,blank=True)
    class Meta:
        db_table='blog_db_friendlylink'
        verbose_name = '友情链接'
        verbose_name_plural= verbose_name
# 博客信息模型类
class Post(models.Model):
    user = models.ForeignKey('user.BlogUser',blank=False,verbose_name="作者",on_delete=models.CASCADE)
    category = models.ForeignKey(BlogCategory,verbose_name='博客分类',on_delete=models.CASCADE,blank=False)
    tags = models.CharField(max_length=2,verbose_name='标签')
    content = models.TextField(verbose_name="内容")
    title = models.CharField(max_length=20,verbose_name='标题')
    create_date = models.DateTimeField(default=timezone.now,verbose_name="发布时间")
    views = models.IntegerField(default=0,verbose_name="浏览数")
    # 博客照片先默认为空
    cover = models.ImageField(upload_to='static/images/post/',default=None,verbose_name="博客图片")
    # 是否推荐博客
    recommend = models.BooleanField(verbose_name='是否推荐博客',default=False)
    str1 = models.CharField(max_length=20,blank=True)
    def __str__(self):
        return  self.title
    class Meta:
        db_table = 'blog_db_post'
        verbose_name = "博客信息"
        verbose_name_plural = verbose_name
# 评论模型类
class Comment(models.Model):
    post = models.ForeignKey(Post,verbose_name='该博客的评论信息',on_delete=models.CASCADE)
    user = models.ForeignKey('user.BlogUser',on_delete=models.CASCADE,verbose_name="作者")
    pud_date = models.DateTimeField(default=timezone.now,verbose_name='评论时间')
    content = models.TextField(verbose_name='评论内容')
    str1 = models.CharField(max_length=20,blank=True)
    def __str__(self):
        return self.content
    class Meta:
        db_table = 'blog_db_comment'
        verbose_name='评论'
        verbose_name_plural = verbose_name