
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView

from .models import BookModel, CategoryModel

class CategoryCreateView(CreateView):
    model = CategoryModel
    context_object_name = 'create_categ'
    fields = ['name','description','parent_category']
    template_name = "book/create_categ.html"
    success_url = '.'
    
    def form_valid(self,form):
        parent_category=form.cleaned_data['parent_category']
        print(parent_category)
        if parent_category is not None:
            print('es hijo')
            parent_category.add_child(name=form.cleaned_data['name'],
                                        description=form.cleaned_data['description'],
                                        parent_category=form.cleaned_data['parent_category']
                                        )
        else:
            print('es root')
            CategoryModel.add_root(name=form.cleaned_data['name'],
                                    description=form.cleaned_data['description'],
                                    parent_category=None
                                    )
        return redirect(self.success_url)

class CategoryListView(ListView):
    model = CategoryModel
    context_object_name = 'list_categ'
    template_name = "book/categ_list.html"

class BookCreateView(CreateView):
    model = BookModel
    fields = ['title','resume', 'publication_date','authors','cover_page','category']
    template_name = "book/create_book.html"
    success_url = '.'
class BookListView(ListView):
    model = BookModel
    context_object_name = 'list_book'
    template_name = "book/book_list.html"



