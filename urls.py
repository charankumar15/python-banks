from django.urls import path
from demo_app.views import welcome_page, bank_account_add, signup, user_login , user_logout , article_list , article_add


urlpatterns =[
    path('welcome/', welcome_page , name='welcome-page'),
    path('bank_account_add/', bank_account_add, name='bank-account-add'),
    path('Signup/', signup, name='signup'),
    path('login/' , user_login , name='login'),
    path('logout/' , user_logout , name='logout'),
    path('article_list/',article_list, name='article-list'),
    path('article_add/', article_add, name='article_add'),

]



