from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .chat import get_response
import json

# Create your views here.
@csrf_exempt
def predict(request, pk):
    data = json.loads(request.body)
    text = data.get("message")
    # TODO: Check if text is valid
    response = get_response(text)
    message = {"answer":response}
    return JsonResponse(message)
