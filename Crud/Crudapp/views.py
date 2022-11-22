from django.shortcuts import render, redirect
from Crudapp.models import book
from Crudapp.forms import book
def index(request):
    x= book.objects.all()
    return render(request, 'book/library.html', {'x': x})
    if upload():
    	upload.save()
    else:
    	return redirect('index')
def update_book(request, book_id):
	book_id = int(book_id)
	try:
		book_sel = book.objects.get(id = book_id)
	except book.DoesNotExist:
		return redirect('index')
def delete_book(request, book_summary):
    book_summary = int(book_summary)
    try:
        book_sel = book.objects.get(id = book_summary)
    except book.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    return redirect('index')

