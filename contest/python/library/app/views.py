from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponse
from django.utils import timezone


from .models import Book


def borrow_book(self, user):
        if self.user_borrowed is not None:
            return False
        self.user_borrowed = user

def Library(request, book_id):
    get_book_users = Book.objects.get(id=book_id)
    # library = Book.objects.all().filter(user_borrowed=request.user.username).values('user_borrowed')
    # print(library)

    if borrow_book:
        
        def creat_instance():
            library = Book.objects.all().values('user_borrowed')
            date = timezone.now()

    
    library2 = list(creat_instance())
    return JsonResponse(
        library2
    )
    # library1 = Book.objects.all().values('user_borrowed')
    # library_list = list(library)[0]
    # date = timezone.now()
    
    # return JsonResponse({
    #     'username':library_list,
    #     'date':date
    # })