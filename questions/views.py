from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from .models import Question
from .serializers import responseQuestionSeializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class getAllQuestions(APIView):
    model=Question
    serializer_class = responseQuestionSeializer
    def get(self,request):
        try:
            questions = self.model.objects.all()
            json_questions = self.serializer_class(data=questions,many=True)
            if(json_questions.is_valid()):
                return JsonResponse({'questions': json_questions.data},status=200)
            else:
                print(json_questions.error_messages)
                return JsonResponse({'questions': []}, status=200)

        except Exception as err:
            print(err.args)
            return JsonResponse({'message': 'Something went wrong'}, status=500)
        