from django.shortcuts import render, HttpResponseRedirect
from ghostpost.models import Broast
from ghostpost.forms import BroastForm
# Create your views here.
def index(request):
    data = Broast.objects.all().order_by('-date')
    for item in data:
        item.sum = item.up - item.down
    return render(request, 'index.html', {'data':data})

def top(request):
    data = Broast.objects.all()
    data = sorted(data, key=lambda i: i.up - i.down, reverse=True)
    for item in data:
        item.sum = item.up - item.down
    return render(request, 'index.html', {'data':data})

def boast(request):
    data = Broast.objects.filter(is_roast=False)
    for item in data:
        item.sum = item.up - item.down
    return render(request, 'index.html', {'data':data})

def roast(request):
    data = Broast.objects.filter(is_roast=True)
    for item in data:
        item.sum = item.up - item.down
    return render(request, 'index.html', {'data':data})

def upvote(request, id):
    target = Broast.objects.get(id=id)
    target.up += 1
    target.save()
    return HttpResponseRedirect('/')

def downvote(request, id):
    target = Broast.objects.get(id=id)
    target.down += 1
    target.save()
    return HttpResponseRedirect('/')

def broastadd(request):
    html = 'base_form.html'
    if request.method == 'POST':
        form = BroastForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Broast.objects.create(
                is_roast = data['is_roast'],
                content = data['content'],
            )
            return HttpResponseRedirect('/')

    form = BroastForm()
    return render(request, html, {'form': form})