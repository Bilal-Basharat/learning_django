from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.response import TemplateResponse
from .forms import PostForm

posts = [
    {
        'id': 1,
        'title': 'First Post',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    },
    {
        'id': 2,
        'title': 'Second Post',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    },
    {
        'id': 3,
        'title': 'Third Post',
        'content': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.',
    }
]


# Create your views here.
def post_list(request):

    html_content = ""
    for post in posts:
        html_content += f'''
            <h1><a href="{post['id']}/">{post['title']}</a></h1>
            <p>{post['content']}</p>
        '''

    return HttpResponse(html_content)


def post(request, id):
    print('print content')

    post = next((p for p in posts if p['id'] == id), None)

    if not post:
        return HttpResponseNotFound("Post not found", status=404)
    
    request.COOKIES['name'] = 'Bilal'

    response = render(request, 'posts/post.html', {'post': post})
    response.set_cookie('name', 'Bilal')
    return response

def delete_cookie(request):
    response = HttpResponse("Cookie deleted")
    response.delete_cookie('name')
    return response

def redirect_url(request, id):
    url = reverse('post', args=[id])
    return HttpResponseRedirect(url)

def not_found(request):
    return HttpResponseNotFound("Page not found", status=404)

def render_post_list(request):

    response = render(request, 'posts/index.html', {'posts': posts})

    response.set_cookie('my_cookie', 'cookie_value', max_age=5)
    response.set_cookie('secure_cookie', 'secure_value', httponly=True, secure=True, samesite='Strict')
    response.set_cookie('name',  'zeeshan', httponly=True, samesite='Strict')
    
    return response

def post_form(request):


    if request.method == 'POST':
        form = PostForm(request.POST)
        if(form.is_valid()):
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            return HttpResponseRedirect('/posts/thank-you')
    else:
        form = PostForm()
    return render(request, 'posts/form.html', {'form': form})

def thank_you(request):
    return HttpResponse("Thank you for submitting the form!")

def set(request):
    # raise Exception("This is a test exception for testing the error handling middleware.")
    return TemplateResponse(request, 'posts/set.html',{'name': 'Bilal'})

def get():
    return HttpResponse("Thank you for calling get method")