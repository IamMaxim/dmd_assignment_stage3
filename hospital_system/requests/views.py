from django.http import HttpResponse, HttpRequest
from django.utils.datastructures import MultiValueDictKeyError

from . import sql_manager


# Create your views here.
def index(request: HttpRequest):
    query = None

    # Try to get query from the arguments. If it is not available, show error
    try:
        query = request.GET["query"]
    except MultiValueDictKeyError:
        pass

    if query is None:
        return HttpResponse("No query passed. FY.")

    # Return response to the query
    return HttpResponse("Response for your query is:\n" + str(sql_manager.execute(query)))
