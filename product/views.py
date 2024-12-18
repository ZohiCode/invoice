from django.shortcuts import render
from product.models import Product
from product.forms import ProductForm
from django.shortcuts import redirect
# Create your views here.
def products(request):
    products = Product.objects.all()
    return render(request, 'products.jinja.html', {'products': products, })


def add_product(request):
    forms = ProductForm
    if request.method == 'POST':
        form = forms(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            print(form.errors)
    else :
        print("not valid")
        
    return redirect('products')
def update_product(request, id):
    forms = ProductForm
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        form = forms(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
        else:
            print(form.errors)
        
    return redirect('products')

def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()

    return redirect('products')