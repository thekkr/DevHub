from django.shortcuts import render
from db_connectors.queires import temp

def home(request):
    pf_df = temp()
    
    context = {
        'total_jobs': len(pf_df),
        'running_jobs_count': len(pf_df[pf_df['status'] == 'RUNNING']),
        'queued_jobs_count': len(pf_df[pf_df['status'] == 'QUEUED']),
    }
    return render(request, 'dashboard/home.html', context)

