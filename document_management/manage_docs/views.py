from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework import viewsets
# from serializers import *
#
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
from .serializers import *
# from django.http import HttpResponse, JsonResponse
# from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


# @csrf_exempt
@api_view(['GET', 'POST'])
def folders_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        folder_obj = FoldersSerializer.objects.all()
        serializer = DocSerializer(folder_obj, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = FoldersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #     return JsonResponse(serializer.data, status=201)
        # return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def folders_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        folder_obj = Digital_Documents.objects.get(pk=pk)
    except Digital_Documents.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        # return HttpResponse(status=404)


    if request.method == 'GET':
        serializer = FoldersSerializer(folder_obj)
        return Response(serializer.data)
        # return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        serializer = FoldersSerializer(folder_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #     return JsonResponse(serializer.data)
        # return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        folder_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        # return HttpResponse(status=204)



# @csrf_exempt
@api_view(['GET', 'POST'])
def doc_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        doc_obj = Digital_Documents.objects.all()
        serializer = DocSerializer( doc_obj, many=True)
        # return JsonResponse(serializer.data, safe=False)

        return Response(serializer.data)

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = DocSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #     return JsonResponse(serializer.data, status=201)
        # return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def doc_detail(request):
    """
    Retrieve, update or delete a code snippet.
    """

    # def get_object(self):
    #     username = self.kwargs.get('username')
    #     slug = self.kwargs.get('slug')
    #
    #     # find the user
    #     user = User.objects.get(username=username)
    #
    #     return Example.objects.get(user=user.id, slug=slug)

    try:
        # doc_obj = Digital_Documents.objects.get(pk=pk)
        folder = request.GET.get('folder')
        topic = request.GET.get('topic')
        print(folder,"F T",topic)
        doc_obj = Digital_Documents.objects.filter(i_folders__name=folder)[0]
        doc_obj = doc_obj.topics_set.all().filter(name=topic).values('i_documents')
        doc_obj = Digital_Documents.objects.get(pk=doc_obj[0]['i_documents'])
        print("DOC_OBJ",doc_obj)

    except Digital_Documents.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        # return HttpResponse(status=404)


    if request.method == 'GET':
        serializer = DocSerializer(doc_obj)
        return Response(serializer.data)
        # return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        serializer = DocSerializer( doc_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #     return JsonResponse(serializer.data)
        # return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        doc_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        # return HttpResponse(status=204)



# @csrf_exempt
@api_view(['GET', 'POST'])
def topics_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        topic_obj = TopicSerializer.objects.all()
        serializer = DocSerializer(topic_obj, many=True)
        # return JsonResponse(serializer.data, safe=False)
        return Response(serializer.data)

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #     return JsonResponse(serializer.data, status=201)
        # return JsonResponse(serializer.errors, status=400)


# @csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
def topics_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        topic_obj = Topics.objects.get(pk=pk)
    except Topics.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
        # return HttpResponse(status=404)


    if request.method == 'GET':
        serializer = TopicSerializer(topic_obj)
        return Response(serializer.data)
        # return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        # data = JSONParser().parse(request)
        serializer = DocSerializer(topic_obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        #     return JsonResponse(serializer.data)
        # return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        topic_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        # return HttpResponse(status=204)