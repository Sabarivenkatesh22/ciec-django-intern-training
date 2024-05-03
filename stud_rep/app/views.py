from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import student
from rest_framework.permissions import AllowAny

class StudentCreateAPIView(APIView):
	permission_classes = (AllowAny,)
	def post(self, request):
		try:
			first_name=request.data["first_name"]
			last_name=request.data["last_name"]
			email_id=request.data["email_id"]
		except Exception as e:
			print("Required fields are missing.")
			return Response({'status': False,'message': "Failed to List tag.",'statuscode': 400},status=status.HTTP_400_BAD_REQUEST)

		student_profile = student.objects.create(
			first_name=first_name,
			last_name=last_name,
			email_id=email_id
		)
		print("student_profile------->>", student_profile)
		return Response({
			'status'	: True,
			'data'		: {},
			'message'	: "Student created successfully.",
			'statuscode': 200},status=status.HTTP_200_OK)