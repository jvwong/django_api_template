from django.contrib.auth import get_user_model

from rest_framework import filters, mixins, generics, pagination,\
    permissions, authentication
from rest_framework.response import Response

from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from .models import Placeholder
from .serializers import PlaceholderSerializer, UserSerializer

User = get_user_model()


class DefaultsMixin(object):
    """
    Default settings for the view authentication, permissions,
    filtering and pagination
    """
    authentication_classes = (
        # authentication.BaseAuthentication,
        # authentication.TokenAuthentication,
    )
    permission_classes = (
        #permissions.IsAuthenticated,
    )
    filter_backends = (
        filters.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    )


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 50
    page_size_query_param = 'page_size'
    max_page_size = 100


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'sprints': reverse('sprint-list', request=request, format=format),
        'task': reverse('task-list', request=request, format=format)
    })


class UserList(DefaultsMixin,
               mixins.ListModelMixin,
               generics.GenericAPIView):
    """
    List all users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    search_fields = (User.USERNAME_FIELD,)
    pagination_class = StandardResultsSetPagination

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class UserDetail(DefaultsMixin,
                 mixins.RetrieveModelMixin,
                 generics.GenericAPIView):
    """
    Retrieve a user instance (pk)
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class PlaceholderList(DefaultsMixin,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin,
                      generics.GenericAPIView):
    """
    List all code sprints, or create a new sprint
    """
    queryset = Placeholder.objects.all()
    serializer_class = PlaceholderSerializer
    search_fields = ('name',)
    ordering_fields = ('name',)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PlaceholderDetail(DefaultsMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin,
                        generics.GenericAPIView):
    """
    Retrieve, update or delete a sprint instance.
    """
    queryset = Placeholder.objects.all()
    serializer_class = PlaceholderSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)