from django.shortcuts import render
from djoser.views import UserViewSet
from rest_framework.decorators import action
from accounts.models import CustomUser
from rest_framework.response import Response


class CustomUserViewSet(UserViewSet):

    @action(["get", "patch", "delete"], detail=False)
    # @action(["get", "put", "patch", "delete"], detail=False)
    def me(self, request, *args, **kwargs):

        self.get_object = self.get_instance
        if request.method == "GET":
            return self.retrieve(request, *args, **kwargs)
        # elif request.method == "PUT":
        #     return self.update(request, *args, **kwargs)
        elif request.method == "PATCH":
            # if 'password' in request.data:
            #     queryset = CustomUser.objects.filter(
            #         password=request.data['password'])
            # else:
            #     return Response(data={'error': 'passwordが未入力です'}, status=500)
            # if queryset.exists():
            #     return self.partial_update(request, *args, **kwargs)
            # else:
            #     return Response(data={'error': 'passwordが違います'}, status=500)
            if 'password' in request.data and 'email' in request.data:
                return Response(data={'error': '変更箇所にパスワードとメールアドレスが含まれています'}, status=500)
            elif 'password' in request.data:
                return Response(data={'error': '変更箇所にパスワードが含まれています'}, status=500)
            elif 'email' in request.data:
                return Response(data={'error': '変更箇所にメールアドレスが含まれています'}, status=500)
            else:
                return self.partial_update(request, *args, **kwargs)
        elif request.method == "DELETE":
            return self.destroy(request, *args, **kwargs)
