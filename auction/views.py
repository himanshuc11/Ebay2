from django.http import HttpResponse
from django.shortcuts import render

from .models import Bid, Comment, Items
from .forms import ItemForm
from django.db.models import Max

# Create your views here.
def index(request):
    items = Items.objects.all()
    return render(request, 'auction/index.html', {"items": items})

def detailed_view(request, id):

    try:
        item = Items.objects.get(id=id)
    except Items.DoesNotExist:
        return HttpResponse('Invalid ID')

    if request.method == "GET":
        comments = Comment.objects.filter(product=item)
        return render(request, 'auction/detailed-item.html', {"item": item, "comments": comments})

    if request.method == "POST":
        if request.user.is_authenticated:
            if 'comment' in request.POST:
                comment = request.POST['comment']
                comment_object = Comment(comment=comment, user=request.user, product=item)
                comment_object.save()
                return HttpResponse('You have successfully commented')
            if 'bid' in request.POST:
                # Disallow owner of product to make a bid
                # Allow bids only greater than minimum bid
                bid = request.POST['bid']
                bid_object = Bid(amount=bid, bidder=request.user, product=item)
                bid_object.save()
                return HttpResponse('Bid was successfully accepted')
        else:
            return HttpResponse('You cannot comment')

def create_item(request):
    if request.method == "GET":
        form = ItemForm()
        return render(request, 'auction/create-item.html', {"form": form})
    if request.method == "POST":
        bounded_form = ItemForm(request.POST, request.FILES)
        if bounded_form.is_valid():
            name = bounded_form.cleaned_data['name']
            description = bounded_form.cleaned_data['description']
            tags = bounded_form.cleaned_data['tags']
            image = bounded_form.cleaned_data['image']
            new_item = Items(name=name, description=description, image=image, owner=request.user)
            new_item.save()

            for tag in tags:
                new_item.tags.add(tag)
            new_item.save()
            
            return HttpResponse('Create a new item')
        else:
            return HttpResponse(bounded_form.errors)


# Make a field called is_active in Items to store if item is for sale or auction for this item has ended
# Details Page, show winner if is_active is False, or show maximum bid in case of multiple bids
# or in case of no bids, show the minimum bid amount


def close_auction(request, id):
    user = request.user
    if not user.is_authenticated:
        return HttpResponse('You need to be logged in')
    try:
        item = Items.objects.get(id=id)
    except Items.DoesNotExist:
        return HttpResponse('Invalid Item')
    
    if item.owner == user:
        bids = Bid.objects.filter(product=item)
        if len(bids) == 0:
            return HttpResponse('There are no bids on the item')
        max_bid_amount = bids.aggregate(Max('amount'))
        max_bid_amount = max_bid_amount["amount__max"]
        bid = bids.get(amount=max_bid_amount)
        v = f"Winner of this product is {bid.bidder}"
        return HttpResponse(v)
    else:
        return HttpResponse('You cannot close the auction')