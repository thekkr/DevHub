from django.shortcuts import render, get_object_or_404
from .models import SoftwareProduct

def product_build_details(request, product_name):
    # Get the product or return 404
    product = get_object_or_404(SoftwareProduct, name=product_name)
    
    # Get all related software images with their associated commands
    software_images = product.software_images.all().prefetch_related(
        'repo_sync',
        'kernel_compilations',
        'vendor_compilation',
        'super_image'
    )
    
    context = {
        'product': product,
        'software_images': software_images,
    }
    
    return render(request, 'build/product_build_details.html', context)

def product_list(request):
    # List all software products
    products = SoftwareProduct.objects.all().prefetch_related('software_images')
    
    context = {
        'products': products,
    }
    
    return render(request, 'build/product_list.html', context)