from django.shortcuts import render
from .queires import temp
import pandas as pd
from io import BytesIO
from django.http import HttpResponse, JsonResponse


# Create your views here.
def pf_jobs_detail(request):
    pf_df = temp()
    
    context = {
        'total_jobs': len(pf_df),
        'running_jobs_count': len(pf_df[pf_df['status'] == 'RUNNING']),
        'queued_jobs_count': len(pf_df[pf_df['status'] == 'QUEUED']),
        'pf_jobs': pf_df.to_dict('records')
    }
    return render(request, 'db_connectors/pf_job_details.html', context)

def failed_builds_dashboard(request):
    # Sample data - replace with your actual data fetching logic
    data = {
        'warehouseid': ['WH1', 'WH1', 'WH2', 'WH3', 'WH3', 'WH3'],
        'warehousename': ['Warehouse A', 'Warehouse A', 'Warehouse B', 'Warehouse C', 'Warehouse C', 'Warehouse C'],
        'promotebuildid': ['PB100', 'PB101', 'PB200', 'PB300', 'PB301', 'PB302'],
        'variantname': ['Variant X', 'Variant Y', 'Variant Z', 'Variant A', 'Variant B', 'Variant C'],
        'Buildstatus': ['Failed', 'Failed', 'Failed', 'Failed', 'Failed', 'Failed'],
        'buildworkflowurl': ['url1', 'url2', 'url3', 'url4', 'url5', 'url6'],
        'builddate': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06']
    }
    df = pd.DataFrame(data)
    
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        warehouse_id = request.POST.get('warehouse_id')
        variants_df = df[df['warehouseid'] == warehouse_id]
        variants_data = variants_df[['variantname', 'buildworkflowurl', 'builddate']].to_dict('records')
        return JsonResponse({'variants': variants_data})
    
    # Group by warehouse to get failure counts
    warehouse_failures = df.groupby(['warehouseid', 'warehousename']).size().reset_index(name='failure_count')
    
    context = {
        'warehouse_failures': warehouse_failures.to_dict('records'),
    }
    return render(request, 'db_connectors/failed_builds_dashboard.html', context)

def warehouse_variants(request, warehouse_id):
    # Sample data - with added warehousename
    data = {
        'warehouseid': ['WH1', 'WH1', 'WH2', 'WH3', 'WH3', 'WH3'],
        'warehousename': ['Warehouse A', 'Warehouse A', 'Warehouse B', 'Warehouse C', 'Warehouse C', 'Warehouse C'],
        'variantname': ['Variant X', 'Variant Y', 'Variant Z', 'Variant A', 'Variant B', 'Variant C'],
        'buildworkflowurl': ['url1', 'url2', 'url3', 'url4', 'url5', 'url6'],
        'builddate': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06']
    }
    df = pd.DataFrame(data)
    
    variants = df[df['warehouseid'] == warehouse_id]
    
    context = {
        'warehouse_name': variants.iloc[0]['warehousename'] if not variants.empty else '',
        'variants': variants.to_dict('records'),
    }
    return render(request, 'db_connectors/warehouse_variants.html', context)