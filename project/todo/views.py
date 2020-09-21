from django.http import HttpResponse

def index(request):
    html = "<html><body>Hello world!</body></html>"
    return HttpResponse(html)