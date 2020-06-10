from django.shortcuts import render, redirect
from employee.models import Article
from accounts.models import User
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

#모든 게시글 정보 불러오기
def employee_all(request):
    articles = Article.objects.all()
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')  # 없으면 1로 지
    posts = paginator.get_page(page)
    return render(request, 'employee/employee_list.html', { 'articles':articles , 'posts':posts})

#카테고리별로 분류하기
def sort1(request):
    articles = Article.objects.filter(menuid="집안일")
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')  # 없으면 1로 지
    posts = paginator.get_page(page)
    return render(request, 'employee/home.html', { 'articles':articles , 'posts':posts})
def sort2(request):
    articles = Article.objects.filter(menuid="짐 옮기기")
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')  # 없으면 1로 지
    posts = paginator.get_page(page)
    return render(request, 'employee/load.html', { 'articles':articles , 'posts':posts})
def sort3(request):
    articles = Article.objects.filter(menuid="펫 서비스")
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')  # 없으면 1로 지
    posts = paginator.get_page(page)
    return render(request, 'employee/pet.html', { 'articles':articles , 'posts':posts})
def sort4(request):
    articles = Article.objects.filter(menuid="역할 대행")
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')  # 없으면 1로 지
    posts = paginator.get_page(page)
    return render(request, 'employee/acting.html', { 'articles':articles , 'posts':posts})
def sort5(request):
    articles = Article.objects.filter(menuid="단거리 배달")
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')  # 없으면 1로 지
    posts = paginator.get_page(page)
    return render(request, 'employee/short.html', { 'articles':articles , 'posts':posts})
def sort6(request):
    articles = Article.objects.filter(menuid="카풀")
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')  # 없으면 1로 지
    posts = paginator.get_page(page)
    return render(request, 'employee/carpool.html', { 'articles':articles , 'posts':posts})
def sort7(request):
    articles = Article.objects.filter(menuid="기타")
    paginator = Paginator(articles, 5)
    page = request.GET.get('page')  # 없으면 1로 지
    posts = paginator.get_page(page)
    return render(request, 'employee/etc.html', { 'articles':articles , 'posts':posts})



#로그인 했을 경우 새 글쓰기
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
        return redirect(f'/employee/feed/{new_article.pk}')
    return render(request, 'employee/new_feed.html')


#세부사항 보기
def detail_feed(request, pk):
    article = Article.objects.get(pk=pk)
    feed_text=article.text
    feed_text_list=feed_text.split('\n')
    return render(request, 'employee/detail_feed.html', {'feed': article, 'feed_text_list':feed_text_list})

#로그인시+본인 작성글만 삭제가능
@login_required
def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)
    check =request.user.id
    if request.method == 'POST':
        if check == article.postid:
            article.delete()
            return redirect('/employee/')  # 첫페이지로 이동하기
        #else:
         #   return redirect('/employee/')
        return render(request, 'employee/remove_feed.html', {'feed': article})

#로그인시+본인 작성글만 삭제가능
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
            return redirect(f'/employee/feed/{ article.pk }')

    return render(request, 'employee/edit_feed.html', {'feed': article})