from django.http import JsonResponse
import json
# Create your views here.


def home(request):
    print(request.body)
    print(request.headers)
    # body = request.body
    # data = {}
    # try:
    #     data = json.loads(body)
    # except:
    #     pass
    # print(data)
    
    
    return JsonResponse({'message':"Hello"})