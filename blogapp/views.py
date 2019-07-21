from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Blog

def home(request):
    blogs = Blog.objects #쿼리셋
    return render(request, 'home.html', {'blogs':blogs})

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request): #new.html을 띄워주는 함수
    return render(request, 'new.html')

#입력받은 내용을 데이터베이스 안에 넣어주는 함수
def create(request):
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date=timezone.datetime.now() #블로그를 작성한 시간을 넣어주는 함수
    blog.save() #쿼리셋 메소드 중 하나. 데이터베이스에 저장하라!
    return redirect('/blog/'+str(blog.id)) #위에있는 함수들 다 처리한 다음에 이 url로 넘어가세요
    #str로 형변화? : blog id는 int형인데 url은 항상 str(문자열)형임. 그래서 맞춰줘야함
    #redirect와 render함수의 차이는? : 어떤 상황에 사용하는지에 따라 이용이 달라짐
    #redirect('https://google.com') 가능 : 프로젝트 외의 url로도 갈 수 있음
    #render : 세번째 인자로 key값을 담아 프로젝트 내에서 나온 결과 내에서 이동 위주