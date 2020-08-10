from grpc_django.interfaces import rpc
from .views import GetUser, ListUsers


rpcs = [
    rpc(name='GetUser', view=GetUser),
    rpc(name='ListUsers', view=ListUsers)
]