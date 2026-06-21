from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

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

    post = next((p for p in posts if p['id'] == id), None)

    if not post:
        return HttpResponseNotFound("Post not found", status=404)

    # html_content = f'''
    #     <h1>{post['title']}</h1>
    #     <p>{post['content']}</p>
    # '''
    # return HttpResponse(html_content)
    return render(request, 'posts/post.html', {'post': post})

def redirect_url(request, id):
    url = reverse('post', args=[id])
    return HttpResponseRedirect(url)

def not_found(request):
    return HttpResponseNotFound("Page not found", status=404)

def render_post_list(request):
    return render(request, 'posts/index.html', {'posts': posts})