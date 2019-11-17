from django.http import HttpRequest, HttpResponse
from django.template import loader



# Create your views here.
def index(request: HttpRequest):
    template = loader.get_template('./index.html')
    return HttpResponse(template.render({}, request))
