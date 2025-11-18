from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Document

# Create your views here.


@permission_required('accounts.can_view', raise_exception=True)
def document_list(request):
    """
    View to list all documents.
    Requires 'can_view' permission.
    
    Groups with access: Viewers, Editors, Admins
    """
    documents = Document.objects.all()
    return render(request, 'accounts/document_list.html', {'documents': documents})


@permission_required('accounts.can_create', raise_exception=True)
def document_create(request):
    """
    View to create a new document.
    Requires 'can_create' permission.
    
    Groups with access: Editors, Admins
    """
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        
        if title and content:
            Document.objects.create(
                title=title,
                content=content,
                created_by=request.user
            )
            return redirect('document_list')
    
    return render(request, 'accounts/document_form.html', {'action': 'Create'})


@permission_required('accounts.can_edit', raise_exception=True)
def document_edit(request, pk):
    """
    View to edit an existing document.
    Requires 'can_edit' permission.
    
    Groups with access: Editors, Admins
    """
    document = get_object_or_404(Document, pk=pk)
    
    if request.method == 'POST':
        document.title = request.POST.get('title', document.title)
        document.content = request.POST.get('content', document.content)
        document.save()
        return redirect('document_list')
    
    return render(request, 'accounts/document_form.html', {
        'document': document,
        'action': 'Edit'
    })


@permission_required('accounts.can_delete', raise_exception=True)
def document_delete(request, pk):
    """
    View to delete a document.
    Requires 'can_delete' permission.
    
    Groups with access: Admins only
    """
    document = get_object_or_404(Document, pk=pk)
    
    if request.method == 'POST':
        document.delete()
        return redirect('document_list')
    
    return render(request, 'accounts/document_confirm_delete.html', {'document': document})

