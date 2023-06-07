from django.shortcuts import render
from myapp.models import User

def profile(request, pk):
    user_profile = User.objects.get(id=pk)
    context = {'user_profile': user_profile}
        
    return render(request, "page/profile.html", context)