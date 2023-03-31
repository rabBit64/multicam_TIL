from django.shortcuts import render
import random
# Create your views here.
def index(request):
  context = {
    'name' : 'Harry',
  }
  return render(request, 'articles/index.html', context)

def today_dinner(request):
  foods = ['볶음밥', '보쌈', '써브웨이', '치킨', '삼겹살']
  context = {
    'foods': random.choice(foods),
  }
  return render(request, 'articles/today_dinner.html', context)

def throw(request):

  return render(request, 'articles/throw.html')

def catch(request):
  data = request.GET.get('message')
  context = {
    'data': data,
  }
  return render(request, 'articles/catch.html', context)

def lotto_create(request):
  return render(request, 'articles/lotto_create.html')


def index(request):
  return render(request, 'articles/index.html')