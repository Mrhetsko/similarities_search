from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Item, Search
from .serializers import ItemSerializer, SearchItemResponse, GetResultsRequest, SearchItemRequest, GetResultsResponse
from .helper import calculate_similarity
from drf_spectacular.utils import extend_schema


def index(request):
    return render(request, 'similarity/index.html')


# API part
@extend_schema(
    request=ItemSerializer,
    responses={201: ItemSerializer},
    description='Add new item to database'
)
@api_view(['POST'])
def add_item(request):

    serializer = ItemSerializer(data=request.data, many=False)
    if serializer.is_valid():
        serializer.save()
    return Response(status=status.HTTP_201_CREATED, data=serializer.data)


@extend_schema(
    request=SearchItemRequest,
    responses={200: SearchItemResponse},
    description='Search similarities in database by "search_input". Return "search_id"')
@api_view(['POST'])
def search_items(request):
    try:
        search_input = request.data['search_input']
        if search_input:
            all_items = Item.objects.all()
            items_dict = {}
            for i in all_items:
                items_dict[i.id] = i.description
            db_indexes = calculate_similarity(search_input=search_input, item_dict=items_dict)
            search = Search.objects.create(search_input=search_input,
                                           similarity_indexes=db_indexes)
            search.save()
            context = {'search_id': search.id}
            return Response(status=status.HTTP_200_OK, data=context)

        else:
            context = {'Search': 'No input prompt'}
            return Response(status=status.HTTP_400_BAD_REQUEST, data=context)

    except Exception as err:
        print(err)
        context = {'error': err}
        return Response(status=status.HTTP_400_BAD_REQUEST, data=context)


@extend_schema(
    request=GetResultsRequest,
    responses={200: GetResultsResponse},
    description='Get search results by id"')
@api_view(['POST'])
def get_search_results(request):
    search_id = request.data['search_id']
    # print(search_id)
    if search_id:
        try:
            search_item = Search.objects.get(pk=search_id)
            similarity_item_indexes = search_item.similarity_indexes
            similarity_items = Item.objects.filter(id__in=similarity_item_indexes)
            items_serializer = ItemSerializer(similarity_items, many=True)

            return Response(status=status.HTTP_200_OK, data=items_serializer.data)

        except ObjectDoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    else:
        context = {'Search_id': 'No "search_id" in request'}
        return Response(status=status.HTTP_400_BAD_REQUEST, data=context)
