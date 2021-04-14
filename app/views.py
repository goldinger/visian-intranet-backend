from django.http import JsonResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated

from app.models import Person
from app.serializers import PersonSerializer


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def persons(request):
    return JsonResponse(PersonSerializer(Person.objects.all(), many=True).data, safe=False)
