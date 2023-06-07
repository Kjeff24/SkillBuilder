from django.shortcuts import render

# url does not exist
def custom_404(request):
    return render(request, 'myapp/404.html', status=404)