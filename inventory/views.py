from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
from itertools import chain
from django.core.paginator import Paginator
from . import form as fm 
from .models import Item, Outgoing, Incoming

# add item
@login_required
def add_item(request):
    if request.method == 'POST':
        form = fm.AddItemForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.created_by = request.user
            var.save()
            messages.success(request, 'Item created and saved to database')
            return redirect('add-item')
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('add-item')
    else:
        form = fm.AddItemForm()
        context = {'form':form}
    return render(request, 'inventory/add_item.html', context)

# update item 
@login_required
def update_item(request, pk):
    item = Item.objects.get(pk=pk)

    if request.method == 'POST':
        form = fm.UpdateItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item information has been updated and saved to Database')
            return redirect('item-details', item.pk)
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('update-item', item.pk)
    else:
        form = fm.UpdateItemForm(instance=item)
        context = {'form':form, 'item':item}
    return render(request, 'inventory/update_item.html', context)

# delete item
@login_required
def delete_item(request, pk):
    item = Item.objects.get(pk=pk)
    item.delete()
    messages.success(request, 'Item and records have been deleted from the database')
    return redirect('all-items')

# all items
def all_items(request):
    item_list = Item.objects.all()
    paginator = Paginator(item_list, 10)  # Show 10 items per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'items': page_obj}
    return render(request, 'inventory/all_items.html', context)

# item details 
@login_required
def item_details(request, pk):
    item = Item.objects.get(pk=pk)

    all_outgoing = item.outgoing_set.all()
    all_incoming = item.incoming_set.all()

    # Combine and sort
    all_history = sorted(
        chain(all_incoming, all_outgoing), 
        key=lambda tx: tx.timestamp,
        reverse=True
    )

    # Filter by date range from GET parameters
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        try:
            start_dt = datetime.strptime(start_date, '%Y-%m-%d')
            end_dt = datetime.strptime(end_date, '%Y-%m-%d')

            all_history = [
                record for record in all_history 
                if start_dt.date() <= record.timestamp.date() <= end_dt.date()
            ]
        except ValueError:
            messages.warning(request, 'Invalid date format. Use YYYY-MM-DD.')

    # Paginate
    paginator = Paginator(all_history, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'item': item,
        'all_history': page_obj,
        'start_date': start_date,
        'end_date': end_date,
    }
    return render(request, 'inventory/item_details.html', context)

# give item
@login_required
def give_item(request, pk):
    item = Item.objects.get(pk=pk)

    if request.method == 'POST':
        form = fm.GiveItemForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.item = item
            var.user = request.user
            var.quantity_remaining = item.quantity - var.quantity_given 
            item.quantity = var.quantity_remaining

            if item.quantity < 0:
                messages.warning(request, f'Cannot give out {var.quantity_given}. Item low in stock.')
                return redirect('item-details', item.pk)
            
            var.save() 
            item.save()
            messages.success(request, f'You just gave out {item.name} - {var.quantity_given}. Information saved in Database ')
            return redirect('item-details', item.pk)
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('give-item', item.pk)
    else:
        form = fm.GiveItemForm()
        context = {'form':form, 'item':item}
    return render(request, 'inventory/give_item.html', context)

# receive item
@login_required
def receive_item(request, pk):
    item = Item.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = fm.ReceiveItemForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.item = item 
            var.user = request.user
            var.quantity_remaining = item.quantity + var.quantity_received 
            item.quantity = var.quantity_remaining
            var.save() 
            item.save()
            messages.success(request, f'You just received {item.name} - {var.quantity_received}. Information saved in Database')
            return redirect('item-details', item.pk)
        else:
            messages.warning(request, 'Something went wrong. Please check form inputs')
            return redirect('receive-item', item.pk)
    else:
        form = fm.ReceiveItemForm()
        context = {'form':form, 'item':item}
    return render(request, 'inventory/receive_item.html', context)

# search item
@login_required
def search_item(request):
    if request.method == 'GET':
        query = request.GET.get('q')

        results = Item.objects.filter(name__icontains=query)

        context = {'results':results, 'query':query}
        return render(request, 'inventory/search_item.html', context)
