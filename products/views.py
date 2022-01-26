from django.http import Http404
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Review
from .forms import ProductForm, ProductReviewForm
from wishlist.models import Wishlist


def all_products(request):
    """ 
    A view to show all products, including sorting and search queries 
    """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    for product in products:
        reviews = Review.objects.filter(product=product)

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any \
                                            search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'
    product_count = products.count()

    products_paginator = Paginator(products, 8)
    page_num = request.GET.get('page')

    page = products_paginator.get_page(page_num)

    context = {
        'products': products,
        'page': page,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
        'product_count': product_count
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ 
    A view to show individual product details 
    """

    product = get_object_or_404(Product, pk=product_id)
    review_form = ProductReviewForm(data=request.POST or None)

    reviews = Review.objects.filter(product=product)
    number_of_reviews = reviews.count()

    try:
        wishlist = get_object_or_404(Wishlist, username=request.user.id)
    except Http404:
        is_product_in_wishlist = False
    else:
        is_product_in_wishlist = bool(product in wishlist.products.all())

    context = {
        'product': product,
        'is_product_in_wishlist': is_product_in_wishlist,
        'review_form': review_form,
        'reviews': reviews,
        'number_of_reviews': number_of_reviews,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    A view to add a product
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    # post handler
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            # Error on form
            messages.error(request, 'Failed to add product. '
                                    'Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    A view to add a product

    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                                     Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    A view to delete a product
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


@login_required
def add_review(request, product_id):
    """
    A view to add a review to a product
    """
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        review_form = ProductReviewForm(request.POST)

        if review_form.is_valid():
            already_reviewed = Review.objects.filter(product=product,
                                                     user=request.user)
            if not already_reviewed:
                Review.objects.create(
                        product=product,
                        user=request.user,
                        product_rating=request.POST['product_rating'],
                        review_text=request.POST['review_text'],
                )
                messages.info(request, 'Successfully added a review!')
            else:
                messages.error(request, 'You have already reviewed '
                                        'this product!')
            return redirect(reverse('product_detail', args=[product.id]))

        messages.error(request, 'Failed to add product review')
    messages.error(request, 'Invalid Method.')
    return redirect(reverse('product_detail', args=[product.id]))


@login_required
def edit_review(request, product_id,):
    """
    Edit exisiting review
    """

    review = get_object_or_404(Review, pk=product_id)
    product = review.product
    if request.user != review.user:
        messages.error(request, (
                                'You have no permission to access this page'
                                ))
        return redirect('product_detail')
    if request.method == 'POST':
        review_form = ProductReviewForm(request.POST, instance=review)

        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            messages.success(request, 'Successfully updated your review!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product review')
    else:
        review_form = ProductReviewForm(instance=review)
        messages.info(request, 'You are editing your review for ' +
                      f'{review.product.name}')

    template = 'products/edit_review.html'
    context = {
        'review_form': review_form,
        'review': review,
    }

    return render(request, template, context)


@login_required
def delete_review(request, product_id, review_user):
    """
    A view to delete a review to a product
    """
    product = get_object_or_404(Product, pk=product_id)
    review = get_object_or_404(
        Review, product=product, user__username=review_user)

    if request.user != review.user and not request.user.is_superuser:
        messages.error(request, "Sorry, you don't have permission to do that.")
        return redirect(reverse('home'))
    if request.method == 'POST':
        review.delete()
        messages.info(request, 'Your review was deleted')
    else:
        messages.error(request, 'Invalid request')
    return redirect(reverse('product_detail', args=[product.id]))


def sale_items(request):
    """
    A view to display all sale items
    """
    sale_items = None
    sale_items = Product.objects.exclude(pre_sale_price__isnull=True)
    sale_items_count = sale_items.count()

    context = {
        'sale_items': sale_items,
        'sale_items_count': sale_items_count
    }
    return render(request, 'products/sale_items.html', context)
