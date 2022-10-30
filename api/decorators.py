
from django.http import JsonResponse

def is_auth_user(function):
    def wrapper(request, *args, **kwargs):
        try:
            apiKey = request.headrs.get('api-key')
            if apiKey != 'adfadf@!398989R2KYHdfdfd88':
                return JsonResponse(data={
                    'message': 'not authorized',
                    'status': '-1'
                }, status=400)
        except Exception as e:
            return JsonResponse(data={
                    'message': str(e),
                    'status': '-1'
                }, status=400)
        return function(request, *args, **kwargs)
    return wrapper