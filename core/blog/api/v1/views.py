from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .serializers import PostSerializer,CategorySerializer
from ...models import Post,Category
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework import viewsets



# Define method to get posts and send them
"""
@api_view(["GET","POST"]) 
@permission_classes([IsAuthenticatedOrReadOnly])
def postlist(request):
    if request.method == "GET":
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
        
        @api_view(["GET","PUT","DELETE"]) 
@permission_classes([IsAuthenticatedOrReadOnly])
def postDetail(request,id):
    post = get_object_or_404(Post,pk=id)
    if request.method == "GET":
        serializer =PostSerializer(post)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == "DELETE":
        post.delete()
        return Response({"detail":"item remove"},status=status.HTTP_204_NO_CONTENT)
      """
      
      
'''class PostList(APIView):
    """
    getting a list of posts and creating new post
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    
    def get(self,request):
        """
        retrieving a list of posts
        """
        posts = Post.objects.filter(status=True)
        serializer = PostSerializer(posts,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        """
        creating a post with provided data
        """
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        '''
        
'''class PostDetail(APIView):
    """
    getting a detail of post and edit plus removing it
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    
    def get(self,request,id):
        """ retrieving the post data """
        post = get_object_or_404(Post,pk=id,status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def put(self,request,id):
        """editing the post data"""
        post = get_object_or_404(Post,pk=id,status=True)
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,id):
        """ delete the post object """
        post = get_object_or_404(Post,pk=id,status=True)
        post.delete()
        return Response({"detail":"item remove"},status=status.HTTP_204_NO_CONTENT)        
'''
          
'''class PostDetail(APIView):
    """
    getting a detail of post and edit plus removing it
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    
    def get(self,request,id):
        """ retrieving the post data """
        post = get_object_or_404(Post,pk=id,status=True)
        serializer = self.serializer_class(post)
        return Response(serializer.data)
    
    def put(self,request,id):
        """editing the post data"""
        post = get_object_or_404(Post,pk=id,status=True)
        serializer = PostSerializer(post,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self,request,id):
        """ delete the post object """
        post = get_object_or_404(Post,pk=id,status=True)
        post.delete()
        return Response({"detail":"item remove"},status=status.HTTP_204_NO_CONTENT)

        
'''
    
'''class PostList(ListCreateAPIView):
    """
    getting a list of posts and creating new post
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
        
'''

'''class PostViewSet(viewsets.ViewSet):
    """
    getting a list of posts and creating new post
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    
    def list(self,request):
        serializer = self.serializer_class(self.queryset,many=True)
        return Response(serializer.data)
    
    def create(self, request):
     return Response({"detail": "Not implemented yet."}, status=501)

    def retrieve(self, request, pk=None):
     return Response({"detail": "Not implemented yet."}, status=501)

    def update(self, request, pk=None):
     return Response({"detail": "Not implemented yet."}, status=501)

    def partial_update(self, request, pk=None):
     return Response({"detail": "Not implemented yet."}, status=501)
 
    def destroy(self, request, pk=None):
     return Response({"detail": "Not implemented yet."}, status=501)
    
    '''
        
'''class PostDetail(RetrieveUpdateDestroyAPIView):
    """
    getting a detail of post and edit plus removing it
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
        
        '''
        
        
class PostModelViewSet(viewsets.ModelViewSet):
    """
    getting a list of posts and creating new post
    """
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=True)
    
        
class CategoryModelViewSet(viewsets.ModelViewSet):
    
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()    
        
