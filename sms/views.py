from django.shortcuts import HttpResponse
def home(request):
    return HttpResponse("<center><h1>Welcome To University Managmnet System<h1></center>")