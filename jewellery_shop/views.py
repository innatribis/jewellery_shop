from django.shortcuts import render, get_object_or_404
from .models import Category, Collection, Finishing, Product, Gems_for_Products, Metals_for_Products
from cart.forms import CartAddProductForm

def product_list(request, category_slug=None, collection_slug=None, finishing_slug=None):
    category = None
    collection = None
    finishing = None
    categories = Category.objects.all()
    collections = Collection.objects.all()
    finishings = Finishing.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    if collection_slug:
        collection = get_object_or_404(Collection, slug=collection_slug)
        products = products.filter(collection=collection)
    if finishing_slug:
        finishing = get_object_or_404(Finishing, slug=finishing_slug)
        products = products.filter(finishings=finishing)
    return render(request,
                  'jewellery_shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'collection': collection,
                   'collections': collections,
                   'finishing': finishing,
                   'finishings': finishings,
                   'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    gems=Gems_for_Products.objects.filter(product=product)
    metals=Metals_for_Products.objects.filter(product=product)
    finishings = product.finishings.all()
    cart_product_form = CartAddProductForm()
    
    return render(request,
                  'jewellery_shop/product/detail.html',
                  {'product': product,
                   'gems': gems,
                   'metals': metals,
                   'finishings': finishings,
                   'cart_product_form': cart_product_form})
