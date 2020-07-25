import json
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status, authentication, permissions
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseServerError
from django.conf import settings

from .user import UserSerializer
from quantumapi.models import UserProfile, Credit, Image, User

# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from rest_framework.authtoken.models import Token
# from django.contrib.auth import login, authenticate
# from quantumapi.models import ImageForm
# from quantumapi.auth0_views import requires_scope


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        url = serializers.HyperlinkedIdentityField(view_name='userprofile', lookup_field='id')
        fields = ('id', 'address', 'image', 'credits', 'user', )
        depth = 1
        extra_kwargs = {'password': {'write_only': True}}


class UserProfiles(ViewSet):
    # permission_classes = [permissions.AllowAny]
    # authentication_classes = [authentication.TokenAuthentication]


    def list(self, request):
        try:
            userprofiles = UserProfile.objects.all()
            email = self.request.query_params.get('email', None)
            user_id = self.request.query_params.get('userId', None)

            if email is not None:
                auth_user = User.objects.filter(email=email)
                serializer = UserSerializer(auth_user, many=True, context={'request': request})

            elif user_id is not None:
                userprofile = UserProfile.objects.filter(user_id=user_id)
                serializer = UserProfileSerializer(userprofile, many=True, context={'request': request})

            else:
                serializer = UserProfileSerializer(userprofiles, many=True, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


    def retrieve(self, request, pk=None):
        try:
            userprofile = UserProfile.objects.get(pk=pk)
            serializer = UserProfileSerializer(userprofile, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)


    def update(self, request, pk=None):
        userprofile = UserProfile.objects.get(pk=pk)
        userprofile_user_id = userprofile.user_id
        user = User.objects.get(pk=userprofile_user_id)
        email = self.request.query_params.get('email', None)

        userprofile.address = request.data["address"]
        userprofile.image_id = request.data["image_id"]
        userprofile.save()
        return Response({}, status=status.HTTP_204_NO_CONTENT)


    def destroy(self, request, pk=None):
        try:
            userprofile = UserProfile.objects.get(pk=pk)
            userprofile.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        except UserProfile.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.profile = UserProfile(user=self)
    #     super(UserProfile, self).save(*args, **kwargs)
