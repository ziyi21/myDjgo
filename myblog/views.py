from django.shortcuts import render, render_to_response, get_object_or_404
# from django.http import HttpResponse, Http404
from .models import Articles, BlogType


# Create your views here.
def hello_ziyi(request):
    return render(request, 'blog/index.html', {
        'data': "hello ziyi",
    })

# 原始版
# def article_detail(request, article_id):
#     try:
#         article = Articles.objects.get(id=article_id)
#     except Articles.DoesNotExist:
#         raise Http404("该网页不存在")
#     context = {'article_obj': article}
#     return render_to_response('blog/article_detail.html', context)
#     # return HttpResponse("<h2>文章标题：{}</h2><br>文章内容：{}".format(article.title, article.content))


# 简洁版文章详情页
def article_detail(request, article_id):
    article = get_object_or_404(Articles, pk=article_id)
    context = {'article_obj': article}
    return render_to_response('blog/article_detail.html', context)


# 文章列表
def article_list(request):
    # articles = Articles.objects.all()
    articles = Articles.objects.filter(is_deleted=False)
    context = {'articles': articles, 'articles_count': Articles.objects.all().count()}
    return render_to_response('blog/article_list.html', context)


# 博客类型
def article_with_type(request, blog_type_pk):
    # articles = Articles.objects.all()
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    context = {'articles': Articles.objects.filter(blog_type=blog_type), 'blog_type': blog_type}
    return render_to_response('blog/article_with_type.html', context)
