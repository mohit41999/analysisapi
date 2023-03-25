from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *



class FieldApiView(APIView):
    serializer_class = FieldSerializer
    def get(self, request):
        allFeilds = Field.objects.all().values()
        return Response({"Message": "List of Feild", "Field list": allFeilds})

    def post(self, request):
        print('Request data is : ',request.data)
        serializer_obj=FieldSerializer(data=request.data)
        if(serializer_obj.is_valid()):
            Field.objects.create(
                                # id=serializer_obj.data.get("id"),
                                Name=serializer_obj.data.get("Name"),
                                Company=serializer_obj.data.get("Company"),
                                Role=serializer_obj.data.get("Role"),
                                Date=serializer_obj.data.get("Date"),
                                InternshipDuration=serializer_obj.data.get("InternshipDuration"),
                                Intake=serializer_obj.data.get("Intake")
                        )

        # field = Field.objects.all().filter(id=request.data["id"]).values()
        field = Field.objects.all().values()
        return Response({"Message": "Fields added!", "Field": field})
