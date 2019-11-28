import json

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
    response = sql_manager.execute(query)

    print('gonna execute', request)
    if 'second_query' in query:
        l = [[str(x[0]), x[1]] for x in response]
    # elif 'third_query' in query:
    #     pass
    elif 'fourth_query' in query:
        l = [int(x[0]) for x in response]
    else:
        l = [x for x in response]

    return HttpResponse(json.dumps(l))
