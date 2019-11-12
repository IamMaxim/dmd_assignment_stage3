from django.http import HttpResponse

from . import sql_manager


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.\n" + str(sql_manager.execute("SELECT * FROM auth_user")))
