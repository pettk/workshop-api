from rest_framework.response import Response
from rest_framework.views import APIView
from .models import seed
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializer import CustomTokenObtainPairSerializer, RequestBody
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions, status


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

#only "admin1" can do all actions
class AccountPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.username == 'admin1':
                return True
            else:
                if request.method == 'GET':
                    return True
                else:
                    return False

class SeedsList(APIView):
    permission_classes = [IsAuthenticated, AccountPermission]
    serializer_class = RequestBody

    def get(self, request):
        seeds = list(seed.find())
        return Response(seeds)

    def post(self, request):
        serializer = RequestBody(data = request.data)
        if serializer.is_valid():
            seed_data = serializer.validated_data
            seed_data["_id"] = self.get_next_id()
            inserted_product = seed.insert_one(seed_data)
            return Response({"message": "Product added successfully", "new_data": str(inserted_product)})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_next_id(self):
 
        max_id_seed = seed.find_one(sort=[("_id", -1)], projection={"_id": 1})

        if max_id_seed:
            max_id = max_id_seed["_id"]
        else:
            max_id = 0


        next_id = max_id + 1
        return next_id

class SeedDetail(APIView):
    permission_classes = [IsAuthenticated, AccountPermission]
    serializer_class = RequestBody
    
    def get(self, request, pk):
        
        seed_find = seed.find_one({"_id": (pk)})
        if seed_find:
            return Response(seed_find)
        else:
            return Response({"message": "Product not found"}, status=404)

    def put(self, request, pk):
        serializer = RequestBody(data = request.data)
        if serializer.is_valid():
            seed_data = serializer.validated_data
            seed.replace_one({"_id": (pk)}, seed_data)
            return Response({"message": "Product updated successfully"})

    def delete(self, request, pk):
        seed.delete_one({"_id": (pk)})
        return Response({"message": "Product deleted successfully"})
