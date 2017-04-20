from django.shortcuts import redirect, render
from lists.models import Item, List
from lists.forms import ItemForm
from django.core.exceptions import ValidationError

# Create your views here.
def home_page(request):
    return render(request,'home.html',{'form': ItemForm()})

def view_list(request, list_id):
    list_ = List.objects.get(id = list_id)
    error = None

    if request.method == 'POST':
        try:
            item = Item(text=request.POST['text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(list_)
        except ValidationError:
            error = "You can't have an empty list item"

    items = Item.objects.filter(list=list_)
    return render(request, 'list.html', {'items': items, 'list': list_, 'error': error, 'form': ItemForm()})

def new_list(request):
    list_ = List.objects.create()
    item = Item.objects.create(text=request.POST['text'], list = list_)
    try:
        item.full_clean()
        item.save()
    except ValidationError:
        list_.delete()
        error = "You can't have an empty list item"
        return render(request, 'home.html',{'error': error, 'form': ItemForm()})
    return redirect(list_)

