from django.http import HttpResponse

def CustomFunctionMiddleware(get_response):
    # one time configuration and initialization
    print("CustomFunctionMiddleware initialized")
    
    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("CustomFunctionMiddleware: Before view")

        response = get_response(request)
        # response = HttpResponse("Custom Function based middleware")

        # Code to be executed for each request/response after
        # the view is called.
        print("CustomFunctionMiddleware: After view")

        return response
    
    return middleware

class CustomClassMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print("CustomClassMiddleware initialized")

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print("CustomClassMiddleware: Before view")
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.
        print("CustomClassMiddleware: After view")

        return response
    
    def process_view(self, request, view_func, view_args, view_kwargs):
        # print("self: ", self)
        # print("request: ", request)
        # print("view_func: ", view_func)
        # print("view_args: ", view_args)
        # print("view_kwargs: ", view_kwargs)
        # print("CustomClassMiddleware: process_view") 
        # return HttpResponse("Custom Class based middleware - process_view")
        return None
    
    def process_exception(self, request, exception):
        print("Exception: ", exception)
        return None
    
    def process_template_response(self, request, response):
        print("CustomClassMiddleware: process_template_response")
        response.context_data['context_from_template_hook'] = 'This is a context variable added by CustomClassMiddleware'
        return response