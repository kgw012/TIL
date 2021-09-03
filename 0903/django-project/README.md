# PJT 04



### 목차

1. [A. 프로젝트 구조](#a-프로젝트-구조)
2. [B. Model](#b-model)
3. [C. Admin](#c-admin)
4. [D~E. URL & View & Template](#de-url-view-template)
   * [E-1. 공유 템플릿 생성 및 사용](#e-1-공유-템플릿-생성-및-사용)
   * [E-2. 전체 영화 목록 조회](#e-2-전체-영화-목록-조회)
   * [E-3. 새로운 영화 작성 Form](#e-3-새로운-영화-작성-form)
   * [E-4. 영화 데이터 저장](#e-4-영화-데이터-저장)
   * [E-5. 단일 영화 상세 조회](#e-5-단일-영화-상세-조회)
   * [E-6. 추가기능](#e-6-추가기능)

5. [어려웠던 내용](#어려웠던-내용)
6. [후기](#후기)



---



### A. 프로젝트 구조

1. 가상환경을 설치한 후 활성화합니다.

   ```bash
   $ python -m venv venv
   $ source venv/Scripts/activate
   ```

2. 가상환경에 django를 설치합니다.

   ```bash
   $ pip instal django
   ```

3. django를 통해 프로젝트를 시작합니다.

   ```bash
   $ django-admin startproject pjt04
   ```

4. 프로젝트 폴더로 진입한 후, 앱을 만듭니다.

   ```bash
   $ python manage.py startapp movies
   ```

5. settings.py를 아래와 같이 수정합니다.

   ```python
   # 앱 등록
   INSTALLED_APPS = [
       'movies',
       ...
   ]
   
   # 지역 설정
   LANGUAGE_CODE = 'ko-kr'
   
   TIME_ZONE = 'Asia/Seoul'
   ```



---



### B. Model

1. movies의 models.py에 Movie 모델을 명세에 맞춰 생성합니다.

   ```python
   # models.py
   
   from django.db import models
   
   class Movie(models.Model):
       title = models.CharField(max_length=100)
       overview = models.TextField()
       poster_path = models.CharField(max_length=500)
       created_at = models.DateTimeField(auto_now_add=True)
       updated_at = models.DateTimeField(auto_now=True)
   
   
       def __str__(self):
           return self.title
   ```

2. migration을 만들고 migrate 합니다.

   ```bash
   $ python manage.py makemigrations
   $ pyhton manage.py migrate
   ```



---



### C. Admin

1. admin 계정을 만듭니다.

   ```bash
   $ python manage.py createsuperuser
   ```

2. admin 페이지에서 Movie 를 다룰 수 있도록 admin.py에 추가해줍니다.

   ```python
   # admin.py
   
   from django.contrib import admin
   from .models import Movie
   
   admin.site.register(Movie)
   ```



---



### D~E. URL & View & Template

#### E-1. 공유 템플릿 생성 및 사용

1. 공유 템플릿을 생성하고 사용해야 합니다. 가장 기초가 될 base.html을 django에서 인식하기 위해 settings.py에 디렉토리를 추가해줍니다.

   ```python
   # settings.py
   
   TEMPLATES = [
       {
           ...
           'DIRS': [BASE_DIR / 'templates'],
           ...
       },
   ]
   ```

2. 프로젝트 최상단 디렉토리에서 templates 폴더를 추가하고, 그 안에 base.html을 생성합니다. 

   * 각 html 요소가 들어갈 곳에 block 요소를 content 이름으로 추가합니다.
   * 네비게이션 바를 통해서 index, new로 이동할 수 있도록 합니다.

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="UTF-8">
     <meta http-equiv="X-UA-Compatible" content="IE=edge">
     <meta name="viewport" content="width=device-width, initial-scale=1.0">
     <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
     <title>Movies</title>
   </head>
   <body>
     <nav>
       <ul>
         <li><a href="{% url 'movies:index' %}">Home</a></li>
         <li><a href="{% url 'movies:new' %}">New</a></li>
       </ul>
     </nav>
     {% block content %}
     {% endblock content %}
     <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous"></script>
   </body>
   </html>
   ```

3. pjt04/urls.py 에서 movies 앱 관련 템플릿들은 해당 앱에서 다루도록 include 해줍니다.

   ```python
   # pjt04/urls.py
   
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('movies/', include('movies.urls')),
       path('admin/', admin.site.urls),
   ]
   
   ```

4. movies 폴더에 urls.py를 추가하고, url 매핑에 사용할 app_name도 추가해줍니다.

   ```python
   # urls.py
   
   from django.urls import path
   from . import views
   
   app_name = 'movies'
   urlpatterns = [
       
   ]
   
   ```

5. view를 통해서 이동할 템플릿들을 모아놓을 폴더가 필요합니다. movies 폴더에 templates/movies 폴더를 만듭니다. 앞으로 이 폴더 안에 movies와 관련된 템플릿(html)파일들을 넣습니다.



#### E-2. 전체 영화 목록 조회

1. '' 요청이 들어오면 index.html를 응답하여 전체 목록을 보여줘야 합니다. urls.py에 해당 내용을 추가합니다.

   ```python
   # urls.py
   
   urlpatterns = [
       path("", views.index, name='index'),
   ]
   
   ```

2. views.py로 요청이 이동합니다. index 함수에서 해당 요청을 처리해줍니다.

   * DB에서 영화들의 정보를 모두 가져옵니다.
   * 해당 정보를 template에 보내줍니다.

   ```python
   # views.py
   
   def index(request):
       movies = Movie.objects.all()
       context = {
           'movies': movies,
       }
       return render(request, 'movies/index.html', context)
   
   ```

3. 전체 영화 목록 조회를 할 index.html 페이지를 생성합니다.

   * for문을 통해 영화들을 불러오고, 만약 저장된 영화가 없다면 출력할 내용도 empty를 이용해 추가합니다.
   * 제목을 클릭하면 detail 페이지로 이동해야 합니다. detail 페이지로 이동할 때는 해당하는 movie의 정보가 필요하기 때문에 pk값을 같이 넘겨줍니다.

   ```html
   {% extends 'base.html' %}
   
   {% block content %}
   <h1>Index</h1>
   
   {% for movie in movies %}
   <hr>
     <h3>{{ movie.title }}</h3>
     {% empty %}
     <h3>저장된 영화가 없습니다</h3>
   
   {% endfor %}
   {% endblock content %}
   ```

#### 

#### E-3. 새로운 영화 작성 Form

1. 'new/' 요청이 들어오면 new.html를 응답하여 영화 작성 form을 보여줘야 합니다. urls.py에 해당 내용을 추가합니다.

   ```python
   # urls.py
   
   urlpatterns = [
       ...
       path('new/', views.new, name='new'),
       ...
   ]
   ```

2. views.py 에서 new.html을 응답하도록 내용을 추가합니다.

   ```python
   # views.py
   
   ...
   def new(request):
       return render(request, 'movies/new.html')
   ...
   ```

3. 영화 내용을 입력하는 new.html를 작성합니다.

   * DB의 값을 변경해야 하므로, POST 요청으로 영화를 생성하도록 합니다.
   * POST요청이므로 csrf_token을 추가합니다.

   ```html
   {% extends 'base.html' %}
   
   {% block content %}
   <h1>New</h1>
   <hr>
   <form action="{% url 'movies:create' %}" method="POST">
     {% csrf_token %}
     <label for="title">title</label>
     <input type="text" name="title">
     <br>
     <label for="overview">overview</label>
     <textarea name="overview" cols="30" rows="10"></textarea>
     <br>
     <label for="poster_path">poster_path</label>
     <input type="text" name="poster_path">
     <br>
     <button>작성</button>
   </form>
   {% endblock content %}
   ```

#### 

#### E-4. 영화 데이터 저장

1. new.html 에서 영화 정보를 입력한 후 create 별명의 url로 요청을 보냈습니다. urls.py에서 해당 동작을 수행합니다.

   ```python
   # urls.py
   
   urlpatterns = [
       ...
       path('create/', views.create, name='create'),
       ...
   ]
   ```

2. views.py에서 요청을 받아 DB에 저장합니다.

   * request 객체 안에 담긴 정보들을 Movie 객체에 넣습니다.
   * 객체를 DB에 저장합니다.
   * 저장이 완료되면 index 페이지로 리디렉션합니다.

   ```python
   # views.py
   
   ...
   def create(request):
       title = request.POST.get('title')
       overview = request.POST.get('overview')
       poster_path = request.POST.get('poster_path')
   
       movie = Movie(title=title, overview=overview, poster_path=poster_path)
       movie.save()
   
       return redirect('movies:index')
   ...
   ```

#### 

#### E-5. 단일 영화 상세 조회

1. index.html에서 제목을 클릭하면 상세 조회 페이지로 이동해야 합니다. 해당 내용을 추가합니다.

   * 상세 조회할 페이지가 필요하므로, 해당 영화의 pk값을 GET 방식으로 보냅니다.

   ```html
   ...
   {% for movie in movies %}
   <hr>
     <h3><a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a></h3>
   ...
   ```

2. urls.py에서 detail 요청을 view로 보내줍니다.

   ```python
   # urls.py
   
   ...
   urlpatterns = [
       ...
       path('<int:pk>/', views.detail, name='detail'),
       ...
   ]
   ```

3. views.py에서 해당 요청을 처리합니다.

   * pk가 매개변수로 들어옵니다. pk값을 통해 DB에서 영화 정보를 가져옵니다.
   * 가져온 영화 정보를 템플릿으로 보냅니다.

   ```python
   # views.py
   
   ...
   def detail(request, pk):
       movie = Movie.objects.get(pk=pk)
   
       context = {
           'movie': movie,
       }
       return render(request, 'movies/detail.html', context)
   ...
   ```

4. 템플릿(detail.html)에서 영화 정보를 보여줘야합니다.

   * 영화 정보를 받아와 DTL 문법을 이용하여 보여줍니다.
   * 앞으로 수정, 삭제도 이루어져야 하므로 해당 내용을 미리 넣어줍니다.
   * 수정과 삭제는 DB에 변경사항을 주기 때문에 POST로 동작합니다.

   ```html
   {% extends 'base.html' %}
   {% block content %}
     <h1>Detail</h1>
     <hr>
     <h2>제목 : {{ movie.title }}</h2>
     <p class="text-muted"> {{ movie.updated_at }}</p>
     <p>줄거리 : {{ movie.overview }}</p>
     <p>포스터 : <img src="{{ movie.poster_path }}" class="w-25 img-thumbnail" alt="poster"> </p>
     <div class="d-flex">
       <form action="{% url 'movies:edit' movie.pk %}" method="POST">
         {% csrf_token %}
         <button>수정</button>
       </form>
       <form action="{% url 'movies:delete' movie.pk %}" method="POST">
         {% csrf_token %}
         <button>삭제</button>
       </form>
     </div>
     
   {% endblock content %}
   ```

#### 

#### E-6. 추가기능

1. 수정하기를 구현해야 합니다. detail.html에서 받은 edit 요청을 통해 수정하기 페이지로 이동하도록 urls.py에 추가합니다.

   ```python
   # urls.py
   
   urlpatterns = [
       ...
       path('<int:pk>/edit', views.edit, name='edit'),
       ...
   ]
   
   ```

2. views.py에서 해당 내용을 구현합니다.

   * 요청이 POST가 아닌 경우 index 페이지로 보냅니다.
   * pk값을 통해 DB에서 영화 정보를 가져오고, 해당 정보를 edit.html로 보내줍니다.

   ```python
   # views.py
   
   ...
   def edit(request, pk):
       if request.method == 'POST':
           movie = Movie.objects.get(pk=pk)
   
           context = {
               'movie': movie,
           }
           return render(request, 'movies/edit.html', context)
   
       else:
           return redirect('movies:index')
   ...
   ```

3. edit.html에서 수정 form을 보여줍니다.

   * 수정하는 동작을 update 별명으로 POST 요청합니다. 이 때, pk값을 함께 보냅니다.

   ```html
   {% extends 'base.html' %}
   
   {% block content %}
     <h1>Edit</h1>
     <hr>
     <form action="{% url 'movies:update' movie.pk %}" method="POST">
       {% csrf_token %}
       <label for="title">title</label>
       <input type="text" name="title" value="{{ movie.title }}">
       <br>
       <label for="overview">overview</label>
       <textarea name="overview" cols="30" rows="10">{{ movie.overview }}</textarea>
       <br>
       <label for="poster_path">poster_path</label>
       <input type="text" name="poster_path" value="{{ movie.poster_path }}">
       <br>
       <button>수정</button>
     </form>
   {% endblock content %}
   ```

4. update 요청을 처리해야합니다. urls.py에서 요청을 받아 view로 보냅니다.

   ```python
   # urls.py
   
   ...
   urlpatterns = [
       ...
       path('<int:pk>/update', views.update, name='update'),
       ...
   ]
   
   ```

5. views.py에서 update 요청을 처리합니다.

   * 수정사항들을 request 객체에서 받아옵니다.
   * pk값을 통해 DB에서 해당 영화 정보를 객체로 가져오고 수정합니다.
   * 수정한 내용을 저장합니다.
   * 수정이 완료되면 detail 페이지로 보냅니다.

   ```python
   # views.py
   
   ...
   def update(request, pk):
       title = request.POST.get('title')
       overview = request.POST.get('overview')
       poster_path = request.POST.get('poster_path')
   
       movie = Movie.objects.get(pk=pk)
       movie.title = title
       movie.overview = overview
       movie.poster_path = poster_path
       movie.save()
   
       return redirect('movies:detail', movie.pk)
   ...
   ```

6. 삭제하기를 구현해야 합니다. detail.html에서 받은 delete 요청을 urls.py를 통해 views로 보내줍니다.

   ```python
   # urls.py
   
   ...
   urlpatterns = [...
       path('<int:pk>/delete', views.delete, name='delete'),
   ]
   
   ```

7. views.py에서 삭제하기를 구현합니다.

   * 받아온 pk값을 이용하여 해당 영화를 삭제합니다.
   * 만약 POST요청이 아니라면 수행하지 않습니다.

   ```python
   # views.py
   
   ...
   def delete(request, pk):
       if request.method == 'POST':
           movie = Movie.objects.get(pk=pk)
           movie.delete()
       
       return redirect('movies:index')
   
   ```

   

---

#### 

### 어려웠던 내용

* 그 동안 반복학습을 해서 그런지, 막히는 부분 없이 잘 진행됐다.



---

### 

### 후기

* 페어 프로그래밍을 하려고 하니, 애매하게 알고 있던 개념들을 더 확실하게 알게 되었다.
* 전에 스프링을 배웠어서 MVC 패턴에 익숙했다. 그래서 이번 django를 통한 CRUD 구현은 비교적 쉽게 수행했다.
* 역시 개발은 너무 재밌다!!
* 스프링보다 django가 더 편하다고 느껴졌다.
