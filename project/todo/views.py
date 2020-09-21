from django.http import HttpResponse


def test(request):
    html = "<html><body>Hello world, it's To-Do app!</body></html>"
    return HttpResponse(html)