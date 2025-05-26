from django.shortcuts import render, get_object_or_404, redirect
from .models import Record
from .forms import RecordForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

@login_required
def list_records(request):
    query = request.GET.get('q')
    records = Record.objects.all()
    if query:
        records = records.filter(
            Q(name__icontains=query) |
            Q(salary__icontains=query) |
            Q(age__icontains=query) |
            Q(birthdate__icontains=query) |
            Q(description__icontains=query)
        )
    return render(request, 'records/list.html', {"records": records})

@login_required
def add_record(request):
    if request.method =='POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = RecordForm()
    return render(request, 'records/form.html', {'form': form})

@login_required
def edit_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form = RecordForm(instance=record)
    return render(request, 'records/form.html', {'form': form})

@login_required
def delete_record(request, pk):
    record = get_object_or_404(Record, pk=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('list')
    return render(request, 'records/confirm_delete.html', {'record': record})
# Create your views here.
