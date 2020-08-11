from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import json
from random import choice, randrange

from .models import Users, Comment, Article, Ads, Recomment
from .forms import CommentForm, RecommentForm, UsersForm


from django.contrib.auth.hashers import make_password, check_password


# Create your views here.


def my_login_required(function):
    def wrapper(request, *args, **kw): 
        if not request.session.get('users_id'):

          return HttpResponseRedirect('/login')
        else:
          return function(request, *args, **kw)
    return wrapper



def index(request):
    data = {}

    search = False
    articles = Article.objects.filter(is_visible=True)

    paginator = Paginator(articles, 4)

    page = request.GET.get('page', 1)

    try:
      articles = paginator.page(page)
    except PageNotAnInteger:
      articles = paginator.page(1)
    except EmptyPage:
      articles = paginator.page(paginator.num_pages)

    data['articles'] = articles
    data['users_id'] = request.session['users_id']
    data['search'] = search
    return render(request, 'index.html', data)


def search(request):
    data = {'search': True}
    name = request.GET['name']
    articles = Article.objects.filter(title__icontains=name)


    paginator = Paginator(articles, 4)

    page = request.GET.get('page', 1)

    try:
      articles = paginator.page(page)
    except PageNotAnInteger:
      articles = paginator.page(1)
    except EmptyPage:
      articles = paginator.page(paginator.num_pages)

    data['articles'] = articles
    data['users_id'] = request.session['users_id']

    return render(request, 'index.html', data)

def individual(request, slug):
    data = {}
    count = Ads.objects.count()
    random = randrange(1, count+1)
    article =  Article.objects.get(slug=slug)
    comments = Comment.objects.filter(article=article.pk)
  

    try:
        ad = Ads.objects.get(pk=random)
    except Ads.DoesNotExist:
        ad = None

    numeros = [None]*count
    voltas = 0
    if ad != None:
        if ad.is_visible == False:
            for i in Ads.objects.filter(is_visible=True):
                numeros[voltas] = i.pk
                voltas += 1

            # obs: o del é muito eficiente para tirar o none
            del numeros[-1]
            certo_id = choice(numeros)
            
            ad = Ads.objects.get(pk=certo_id)

    form1 = CommentForm(); form2 = RecommentForm();
    data['form1'] = form1; data['form2'] = form2;

    data = {
        'article': article, 'ad': ad,
        'comments': comments, 'recomments': Recomment.objects.all(), 
        'users_id': request.session['users_id'],
    }

    return render(request, 'individual.html', data)

@my_login_required
def comment(request):
    if request.method == 'POST':
        form1 = CommentForm(data=request.POST, files=request.FILES)
        if form1.is_valid():
            comment = form1.save(commit=False)
            comment.save()

            return redirect('individual', slug=comment.article.slug)
        else:
            return HttpResponse(json.dumps(form1.errors))  


def recomment(request):
    if request.method == 'POST':
        form2 = RecommentForm(data=request.POST, files=request.FILES)
        if form2.is_valid():
            recomment = form2.save(commit=False)
            recomment.save()

            return redirect('individual', slug=recomment.article.slug)
        else:
            return HttpResponse(json.dumps(form2.errors))  


def register(request):
    if request.method == 'POST':
        form = UsersForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            password = user.password
            cripto = make_password(password=password, salt=None, hasher='pbkdf2_sha256')
            
            user.password = cripto
            user.save()

            request.session['users_id'] = user.pk

            return redirect('index')
        else:
            return HttpResponse(json.dumps(form.errors))

    return render(request, 'register.html')


def login(request):
    data = {'alerta': False}

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            users = Users.objects.get(email=email)
        except Users.DoesNotExist:
            users = None

        if users != None:
            corresponde = check_password(password=password, encoded=users.password)
            if corresponde:
                request.session['users_id'] = users.pk
                return redirect('index')
            else:
                return HttpResponse("<h1>Senha errada</h1>")
                data['alerta'] = True        
        else:
            data['alerta'] = True

    return render(request, 'login.html', data)

def logout(request):
    request.session['users_id'] = None

    return redirect('index')    