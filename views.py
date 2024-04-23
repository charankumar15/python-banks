from django.shortcuts import render, redirect
from demo_app.forms import BankAccountModelsForm, SignUpForm, LoginForm , ArticleForm
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from demo_app.models import Article 

User = get_user_model()

@login_required
def welcome_page(request):
    return render(request, "demo_app/welcome.html")

def user_logout(request):
    logout(request)
    return redirect('login')

def bank_account_add(request):
    if request.method == "POST":
        form = BankAccountModelsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome-page')
        else:
            return render(request, "demo_app/bank_account_add.html", {"form": form})
    else:
        form = BankAccountModelsForm()
    return render(request, "demo_app/bank_account_add.html", {"form": form})

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, "demo_app/signup.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = User.objects.filter(username=form.cleaned_data['username']).first()
            login(request, user=user)

            return redirect(request.GET.get('next','/demo_app/welcome/'))

        else:
            print("errors--->", form.error_messages)
            error_messages = form.error_messages
            return render(request, template_name="demo_app/login.html",
                context={"form": form, 'error_messages': error_messages})



          
    else:
        form = LoginForm()
    return render(request, "demo_app/login.html", {"form": form})

def article_list(request):
    articles = Article.objects.all()

    return render(request,template_name= "demo_app/articles.html", 
                  context={"articles":articles})

@login_required
def article_add(request):
    print("user--->", request.user)
    if request.method == "POST":
        form = ArticleForm(request.POST or None )
        if form.is_valid():
            print("data--->", form.cleaned_data)
            article_post = form.save(commit=False)
            print("-->title", article_post.title)
            article_post.article_post_by = request.user
            article_post.save()

            return redirect('article-list')

        else:
            print("errors--->", form.error_messages)
            error_messages = form.error_messages
            # return render(request, template_name="demo_app/login.html",
            #     context={"form": form, 'error_messages': error_messages})
    form = ArticleForm()

    return render(request, template_name="demo_app/article_add.html",
              context={"form": form})


