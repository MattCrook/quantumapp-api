from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from quantumapi.models import UserProfile


class UserProfileSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserProfile
        url = serializers.HyperlinkedIdentityField(
            view_name='userprofile',
            lookup_field='id'
        )
        fields = ('id', 'url', 'first_name', 'last_name', 'username', 'address', 'picURL', 'credits')
        depth = 1


class UserProfiles(ViewSet):
    def create(self, request):
        newuserprofile = UserProfile()

        newuserprofile.first_name = request.data["first_name"]
        newuserprofile.last_name = request.data["last_name"]
        newuserprofile.username = request.data["username"]
        newuserprofile.username = request.data["email"]
        newuserprofile.address = request.data["address"]
        newuserprofile.picURL = request.data["picURL"]
        newuserprofile.rollerCoaster_credits = request.data["credits"]


        newuserprofile.save()
        serializer = UserProfileSerializer(newuserprofile, context={'request': request})
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        try:
            userprofile = UserProfile.objects.get(pk=pk)
            serializer = UserProfileSerializer(userprofile, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def update(self, request, pk=None):
        userprofile = UserProfile.objects.get(pk=pk)
        userprofile.first_name = request.data["first_name"]
        userprofile.last_name = request.data["last_name"]
        userprofile.username = request.data["username"]
        userprofile.email = request.data["email"]
        userprofile.address = request.data["address"]
        userprofile.picURL = request.data["picURL"]
        newuserprofile.rollerCoaster_credits = request.data["credits"]

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

    def list(self, request):
        userprofiles = UserProfile.objects.all()
        serializer = UserProfileSerializer(userprofiles, many=True, context={'request': request})
        return Response(serializer.data)
