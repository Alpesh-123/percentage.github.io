from rest_framework.views import APIView
from .serializers import TeacherSerializer
from rest_framework.response import Response

class CalculatePercentage(APIView):
    def post(self, request):
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            maths = serializer._validated_data['maths']
            chemistry = serializer._validated_data['chemistry']
            physics = serializer._validated_data['physics']
            history = serializer._validated_data['history']
            literature = serializer._validated_data['literature']
            
            total = maths + chemistry + physics + history + literature
            
            percentage = (total / 500) * 100
            
            return Response({'percentage':percentage})
        return Response(serializer.errors)
            
            

