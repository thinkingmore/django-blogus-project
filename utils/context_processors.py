from blog.models import Category

def categories(request):
    # Retrieve all categories and make them available in the context
    categories = Category.objects.all()
    return {'categories': categories}