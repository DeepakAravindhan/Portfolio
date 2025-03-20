# contact_app/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Contact
from django.views.decorators.csrf import csrf_exempt
import json

def portfolio_view(request):
    return render(request, 'portfolio.html')

@csrf_exempt
def contact_form(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            contact = Contact(
                name=data['name'],
                mobile=data['mobile'],
                email=data['email'],
                message=data['message']
            )
            contact.save()
            return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    return JsonResponse({'success': False, 'message': 'Invalid request method'})