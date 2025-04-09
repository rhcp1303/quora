from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('ask/', views.ask_question, name='ask_question'),
    path('question/<int:question_id>/', views.view_question, name='view_question'),
    path('question/<int:question_id>/answer/', views.answer_question, name='answer_question'),
    path('answer/<int:answer_id>/like/', views.like_answer, name='like_answer'),
    path('question/<int:question_id>/upvote/', views.upvote_question, name='upvote_question'),
    path('question/<int:question_id>/downvote/', views.downvote_question, name='downvote_question'),
]
