from django.shortcuts import render, get_object_or_404
from .models import SoftwareProduct
import pandas as pd
import numpy as np
import random
from django.http import JsonResponse
from django.http import HttpResponse
from io import BytesIO
import time
# Create DataFrame with random values
df = pd.DataFrame({
    'Date': pd.date_range(start='2023-01-01', periods=10),
    'Product_ID': np.random.randint(1000, 9999, size=10),
    'Sales': np.random.randint(50, 500, size=10),
    'Price': np.round(np.random.uniform(10.0, 99.99, size=10), 2),
    'Rating': np.random.choice([1, 2, 3, 4, 5], size=10),
    'In_Stock': np.random.choice([True, False], size=10)
})

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

def build_homepage(request):
    # List all software products
    return render(request, 'build/build_homepage.html')

def get_wonnect_and_kernel_tips(request):
    if request.method == 'POST':
        time.sleep(2)
        build_id = request.POST.get('build_id', '')
        
        # Sample dataframe creation
        data = {
            'Component': ['WonNECT', 'Kernel', 'Driver', 'Framework'],
            'Version': [f'1.{random.randint(0,5)}.{random.randint(0,9)}' for _ in range(4)],
            'Status': random.choices(['Stable', 'Beta', 'Alpha'], k=4),
            'Tips': [
                'Use version 1.3+ for better performance',
                'Apply patch XYZ for memory optimization',
                'Update to latest driver for compatibility',
                'Rebuild with flag --enable-feature-abc'
            ],
            'Last_Updated': pd.date_range(end=pd.Timestamp.today(), periods=4).strftime('%Y-%m-%d')
        }
        df = pd.DataFrame(data)
        
        # Handle Excel export request
        if request.POST.get('export_excel') == 'true':
            output = BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                df.to_excel(writer, index=False, sheet_name='Tips')
            output.seek(0)
            response = HttpResponse(
                output.getvalue(),
                content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
            )
            response['Content-Disposition'] = f'attachment; filename="wonnect_tips_{build_id}.xlsx"'
            return response
        
        # Return JSON for AJAX requests
        return JsonResponse({
            'build_id': build_id,
            'table_html': df.to_html(classes='table table-striped', index=False, justify='left')
        })
    
    return render(request, 'build/wconnect_kernel_tips.html')