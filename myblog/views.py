from django.shortcuts import render,render_to_response, get_object_or_404
# from django.http import HttpResponse, Http404
from .models import Articles


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
    articles = Articles.objects.all()
    context = {'articles': articles}
    return render_to_response('blog/article_list.html', context)
