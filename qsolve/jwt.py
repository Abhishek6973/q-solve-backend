from django.http import JsonResponse
from rest_framework_simplejwt.tokens import UntypedToken, TokenError
from rest_framework_simplejwt.authentication import JWTAuthentication

class JWTUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        jwt_auth = JWTAuthentication()
        authorization_header = request.headers.get('Authorization')

        if authorization_header and authorization_header.startswith('Bearer '):
            token = authorization_header.split(' ')[1]
            print("here")

            try:
                # Attempt to decode the token
                validated_token = jwt_auth.get_validated_token(token)
                user = jwt_auth.get_user(validated_token)
                request.user = user
            except TokenError as e:
                return JsonResponse({'error': 'Invalid token'}, status=401)
            except Exception as err:
                print(err.args)

        response = self.get_response(request)
        return response