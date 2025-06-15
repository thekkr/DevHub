from django.shortcuts import render
from db_connectors.queires import temp
import pandas as pd
from io import BytesIO
from django.http import HttpResponse, JsonResponse

data = {
        'warehouseid': ['WH1', 'WH1', 'WH2', 'WH3', 'WH3', 'WH3'],
        'warehousename': ['Warehouse A', 'Warehouse A', 'Warehouse B', 'Warehouse C', 'Warehouse C', 'Warehouse C'],
        'promotebuildid': ['PB100', 'PB101', 'PB200', 'PB300', 'PB301', 'PB302'],
        'variantname': ['Variant X', 'Variant Y', 'Variant Z', 'Variant A', 'Variant B', 'Variant C'],
        'Buildstatus': ['Failed', 'Failed', 'Failed', 'Failed', 'Failed', 'Failed'],
        'buildworkflowurl': ['url1', 'url2', 'url3', 'url4', 'url5', 'url6'],
        'builddate': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06']
    }

def home(request):
    pf_df = temp()
    data = {
        'warehouseid': ['WH1', 'WH1', 'WH2', 'WH3', 'WH3', 'WH3'],
        'warehousename': ['Warehouse A', 'Warehouse A', 'Warehouse B', 'Warehouse C', 'Warehouse C', 'Warehouse C'],
        'promotebuildid': ['PB100', 'PB101', 'PB200', 'PB300', 'PB301', 'PB302'],
        'variantname': ['Variant X', 'Variant Y', 'Variant Z', 'Variant A', 'Variant B', 'Variant C'],
        'Buildstatus': ['Failed', 'Failed', 'Failed', 'Failed', 'Failed', 'Failed'],
        'buildworkflowurl': ['url1', 'url2', 'url3', 'url4', 'url5', 'url6'],
        'builddate': ['2023-01-01', '2023-01-02', '2023-01-03', '2023-01-04', '2023-01-05', '2023-01-06']
    }
    data = pd.DataFrame(data)
    context = {
        'total_jobs': len(pf_df),
        'running_jobs_count': len(pf_df[pf_df['status'] == 'RUNNING']),
        'queued_jobs_count': len(pf_df[pf_df['status'] == 'QUEUED']),
        'unique_warehouses_count': data['warehousename'].nunique(),
        'total_failures_count': len(data)
        
    }
    return render(request, 'dashboard/home.html', context)

