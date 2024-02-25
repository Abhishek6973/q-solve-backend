from rest_framework.views import APIView
from django.http import JsonResponse
import re
import requests
from .serializers import *
import os
import cloudinary.uploader
import uuid
from django.conf import settings
import json

# Create your views here.
class KitLink(APIView):
    def get(self,request):
        href = request.GET.get('url')
        
        if not href:
            return JsonResponse({'error': 'Invalid href'}, status=400)

        try:
            response = requests.get(href)
            response.raise_for_status()
            html_content = response.text

            title_match = re.search(r'<title>(.*?)<\/title>', html_content)
            title = title_match.group(1) if title_match else ""

            description_match = re.search(r'<meta name="description" content="(.*?)"', html_content)
            description = description_match.group(1) if description_match else ""

            image_match = re.search(r'<meta property="og:image" content="(.*?)"', html_content)
            image_url = image_match.group(1) if image_match else ""
            
            return JsonResponse({
                'success': 1,
                'meta': {
                    'title': title,
                    'description': description,
                    'image': {
                        'url': image_url
                    }
                }
            })
        except requests.RequestException as e:
            return JsonResponse({'message': 'Something went wrong'}, status=500)
        
                
class KitImage(APIView):
    def post(self, request):
        try:
            image_file = request.FILES['image']
            random_name = uuid.uuid4().hex

            _, ext = os.path.splitext(image_file.name)

            new_file_name = f'{random_name}{ext}'
            public_id = f'test/{new_file_name}'

            upload_result = cloudinary.uploader.upload(image_file, public_id=public_id)
            file_url=upload_result['url']
            
            return JsonResponse({
                "success" : 1,
                "file": {
                    "url" : file_url,
                }
            }, status=200) 

        except Exception as err:
            print(err.args)
            return JsonResponse({'message': 'something went wrong'}, status=500)
        

class createKitView(APIView):
    serializer_class=createKitSerializer

    def post(self,request):
        try:
            serializer = self.serializer_class(data=request.data)

            if not serializer.is_valid():
                return JsonResponse({'message':'Invalid request data'},status=400)
            
            serializer.save()
            return JsonResponse({'data':'Post uploaded successfully'},status=200)
        except Exception as err:
            print(err.args)
            return JsonResponse({'message':'something went wrong'},status=500)

class getAllKitView(APIView):
    model = KitModel
    def get(self,request):
        try:
            kits=self.model.objects.all()
            json_kits = [{'id': kit.id, 'title': kit.title,'content': kit.content,'created_at': kit.created_at } for kit in kits]
            return JsonResponse({'data': json_kits},status=200)
        except Exception as err:
            print(err.args)
            return JsonResponse({'message':'something went wrong'},status=500)

class deleteKitView(APIView):
    model = KitModel

    def delete(self,request,kitId):
        try:
            kit = self.model.objects.get(id=kitId)
            kit.delete()

            return JsonResponse({'message': 'kit deleted successfully'},status=200)
        except Exception as err:
            print(err.args)
            return JsonResponse({'message':'something went wrong'},status=500)
        
    def get(self,request,kitId):
        try:
            kit = self.model.objects.get(id=kitId)
            json_kit = {
                'id': kit.id,
                'title': kit.title,
                'content': kit.content,
                'created_at': kit.created_at
            }
            return JsonResponse({'data':json_kit},status=200)
        
        except Exception as err:
            print(err.args)
            return JsonResponse({'message':'something went wrong'},status=500)

class getMetaData(APIView):
    model=KitModel
    def get(self,request):
        try:
            kits = self.model.objects.all()
        
            metadata_list = []
            for kit in kits:
                # Parse JSON content
                content = kit.content


                # Find the first image URL
                first_image_url = None
                first_paragraph = None
                for block in content['blocks']:
                    if block['type'] == 'image' and not first_image_url:
                        first_image_url = block['data']['file']['url']

                    elif block['type'] == 'paragraph' and not first_paragraph:
                        paragraph_text = block['data']['text']

                        if len(paragraph_text) > 30:
                            first_paragraph = paragraph_text[:30] + '...'
                        else:
                            first_paragraph = paragraph_text

                    # Break loop if both image URL and paragraph are found
                    if first_image_url and first_paragraph:
                        break

                # Create metadata dictionary for the current post
                metadata = {
                    'id': kit.id,
                    'title': kit.title,
                    'created_at': kit.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                    'imageSrc': first_image_url,
                    'description': first_paragraph
                }

                # Append metadata to the list
                metadata_list.append(metadata)

            return JsonResponse({'data':metadata_list}, status=200)

        except Exception as err:
            print(err.args)
            return JsonResponse({'message':'something went wrong'},status=500) 
