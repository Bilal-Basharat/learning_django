def categories(request):
    categories = ['Technology', 'Health', 'Travel', 'Food', 'Lifestyle']
    return {'categories': categories}