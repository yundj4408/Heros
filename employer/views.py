from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from employer.models import Article
from accounts.models import User
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required


def employer_all(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')  # 없으면 1로 지
    posts = paginator.get_page(page)
    return render(request, 'employer/employer_list.html', { 'articles':articles , 'posts':posts})

def sort1(request):
    articles = Article.objects.filter(menuid="집안일")
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'employer/home.html', { 'articles':articles , 'posts':posts})
def sort2(request):
    articles = Article.objects.filter(menuid="짐 옮기기")
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'employer/load.html', { 'articles':articles , 'posts':posts})
def sort3(request):
    articles = Article.objects.filter(menuid="펫 서비스")
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'employer/pet.html', { 'articles':articles , 'posts':posts})
def sort4(request):
    articles = Article.objects.filter(menuid="역할 대행")
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'employer/acting.html', { 'articles':articles , 'posts':posts})
def sort5(request):
    articles = Article.objects.filter(menuid="단거리 배달")
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'employer/short.html', { 'articles':articles , 'posts':posts})
def sort6(request):
    articles = Article.objects.filter(menuid="카풀")
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'employer/carpool.html', { 'articles':articles , 'posts':posts})
def sort7(request):
    articles = Article.objects.filter(menuid="기타")
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'employer/etc.html', { 'articles':articles , 'posts':posts})




@login_required
def new_feed(request):
    if request.method == 'POST':  # 폼이 전송되었을 때만 아래 코드를 실행
        if request.POST['menuid'] !='게시판선택' and request.POST['title'] != '' and request.POST['price'] != '' and request.POST['text'] != '' and \
                request.POST['place'] != '':
            new_article = Article.objects.create(
                postid = User.objects.get(id = request.user.get_username()),
                menuid=request.POST['menuid'],
                title=request.POST['title'],
                place=request.POST['place'],
                price=request.POST['price'],
                text=request.POST['text']
            )

            # 새글 등록 끝
        return redirect(f'/employer/feed/{new_article.pk}')
    return render(request, 'employer/new_feed.html')



def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)
    feed_text=article.text
    feed_text_list=feed_text.split('\n')
    return render(request, 'employer/detail_feed.html', {'feed': article, 'feed_text_list':feed_text_list})

@login_required
def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)
    check =request.user.id
    if request.method == 'POST':
        if check == article.postid:
            article.delete()
            return redirect('/employer/')  # 첫페이지로 이동하기
        #else:
         #   return redirect('/employer/')
    return render(request, 'employer/remove_feed.html', {'feed': article})
@login_required
def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)
    check = request.user.id
    if request.method == 'POST':
        if check == article.postid:
            article.title = request.POST['title']
            article.place = request.POST['place']
            article.price = request.POST['price']
            article.text = request.POST['text']
            article.save()
            return redirect(f'/employer/feed/{ article.pk }')

    return render(request, 'employer/edit_feed.html', {'feed': article})
# Create your views here.
