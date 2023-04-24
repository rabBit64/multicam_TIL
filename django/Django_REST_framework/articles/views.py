from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleSerializer, ArticleListSerializer


@api_view(['GET', 'POST'])   #이거 필수임!!
def article_list(request):
  #데이터 생성!
  if request.method == 'GET':
    articles = Article.objects.all()
    serializer = ArticleListSerializer(articles,many=True)
    return Response(serializer.data)
  #데이터 조회! 
  elif request.method == 'POST':
    #요청받은 사용자 입력 데이터를 기반으로 ArticleSerializer 인스턴스 생성
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      # 생성 성공 시 201 응답
      return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE','PUT'])
def article_detail(request,article_pk):
  article = Article.objects.get(pk=article_pk)
  if request.method == 'GET':
    serializer = ArticleSerializer(article)
    return Response(serializer.data)
  elif request.method == 'DELETE':
    article.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  elif request.method == 'PUT':
    serializer = ArticleSerializer(article, data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      return Response(serializer.data)