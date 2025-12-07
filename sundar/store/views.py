from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Product


# 1) Product list view
def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})


# Home page view
def home(request):
    # could include featured products or static content
    featured = Product.objects.all()[:6]
    return render(request, 'store/home.html', {'featured': featured})


# 2) Product detail view
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/product_detail.html', {'product': product})


# Helper: get cart dict from session
def _get_cart(request):
    return request.session.get('cart', {})


# 3) Add to cart
def add_to_cart(request, product_id):
    cart = _get_cart(request)
    product = get_object_or_404(Product, id=product_id)

    # If product is not in cart, add it with qty=1; otherwise increment
    pid = str(product_id)
    if pid in cart:
        cart[pid] += 1
    else:
        cart[pid] = 1

    request.session['cart'] = cart
    # Optional: set session.modified = True to ensure save
    request.session.modified = True
    return redirect(reverse('store:cart_view'))


# 4) View cart
def cart_view(request):
    cart = _get_cart(request)
    products = []
    total = 0

    if cart:
        product_ids = [int(pid) for pid in cart.keys()]
        qs = Product.objects.filter(id__in=product_ids)
        for product in qs:
            quantity = cart.get(str(product.id), 0)
            total_price = product.price * quantity
            total += total_price
            products.append({
                'product': product,
                'quantity': quantity,
                'total_price': total_price,
            })

    return render(request, 'store/cart.html', {'cart_items': products, 'total': total})


# 5) Remove from cart
def remove_from_cart(request, product_id):
    cart = _get_cart(request)
    pid = str(product_id)
    if pid in cart:
        del cart[pid]
    request.session['cart'] = cart
    request.session.modified = True
    return redirect(reverse('store:cart_view'))


# 6) Update quantity (POST expected)
def update_quantity(request, product_id):
    if request.method == 'POST':
        qty = int(request.POST.get('quantity', 1))
        cart = _get_cart(request)
        pid = str(product_id)
        if qty <= 0:
            if pid in cart:
                del cart[pid]
        else:
            cart[pid] = qty
        request.session['cart'] = cart
        request.session.modified = True
    return redirect(reverse('store:cart_view'))


