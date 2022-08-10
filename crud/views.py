from functools import partial
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .models import Diary
from .serializers import DiarySerialaizer

class DiaryListApiView(APIView):

	def get(self, request, *args, **kwargs):
		entries = Diary.objects.all()
		serialaizer = DiarySerialaizer(entries, many=True)
		return Response(serialaizer.data,status=status.HTTP_200_OK)

	def post(self, request, *args, **kwargs):
		data = {
			'title': request.data.get('title'),
			'body': request.data.get('body'),
		}
		serialaizer = DiarySerialaizer(data=data)
		if serialaizer.is_valid():
			serialaizer.save()
			return Response(serialaizer.data, status=status.HTTP_201_CREATED)

		return Response(serialaizer.errors,status=status.HTTP_400_BAD_REQUEST)


class DiaryDetailApiView(APIView):

	def get_object(self,id):
		try:
			return Diary.objects.get(id=id)
		except Diary.DoesNotExist:
			return None

	def get(self, request, id,*args, **kwargs):
		entrie = self.get_object(id)
		if not entrie:
			return Response({"res": "Object with entrie id does not exist"}, status =status.HTTP_400_BAD_REQUEST)

		serialaizer = DiarySerialaizer(entrie)
		return Response(serialaizer.data,status=status.HTTP_200_OK)

	def put(self, request, id,*args, **kwargs):
		entrie = self.get_object(id)
		if not entrie:
			return Response({"res": "Object with entrie id does not exist"}, status =status.HTTP_400_BAD_REQUEST)

		data = {
			'title': request.data.get('title') if request.data.get('title')!=None else entrie.title,
			'body': request.data.get('body') if request.data.get('body')!=None else entrie.bosy,
		}

		serialaizer = DiarySerialaizer(instance=entrie,data=data,partial=True)
		if serialaizer.is_valid():
			serialaizer.save()
			return Response(serialaizer.data, status=status.HTTP_201_CREATED)

		return Response(serialaizer.errors,status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, id,*args, **kwargs):
		entrie = self.get_object(id)
		if not entrie:
			return Response({"res": "Object with entrie id does not exist"}, status =status.HTTP_400_BAD_REQUEST)
		entrie.delete()
		return Response({"res":"Object deleted!"},status=status.HTTP_200_OK)




    



